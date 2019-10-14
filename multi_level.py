import cairo
import numpy as np
import random as rnd

from geo_object import corners_to_rectangle
from environment import load_level
from tools import key_to_tool

class MultiLevel:
    def __init__(
        self, levels, tools,
        drop_prob = 0, max_moves = 20,
        out_size = (256,256), scale = (2,2),
    ):
        self.out_size = np.array(out_size, dtype = int)
        self.scale = np.array(scale, dtype = float)
        self.corners = np.array((
            (0, 0),
            out_size,
        )) * self.scale
        self.levels = [
            load_level(level_pack, level, self.out_size * self.scale)
            for level in levels
        ]
        self.drop_prob = drop_prob
        self.max_moves = max_moves
        self.cur_env = None

        self.tools = []
        self.tool_name_to_index = dict()
        for name, tool in key_to_tool.items():
            if name == "move": continue
            index = len(self.tools)
            self.tools.append(tool)
            self.tool_name_to_index[name] = index

        self.start_level()

    def start_level(self):
        self.cur_env = rnd.choice(self.levels)
        self.cur_env.rand_init()
        self.tool = None
        self.moves = 0

        self.remaining_goals = list(cur_env.cur_goal())
        self.goal_reward = 1. / len(self.remaining_goals)

        self.tool_mask = np.zeros(len(self.tools), dtype = bool)
        for tool_name in self.cur_env.enabled_tools:
            if tool_name == "move": continue
            tool_index = self.tool_name_to_index[tool_name]
            self.tool_mask[tool_index] = True

    def stop_level(self):
        self.cur_env.restart()
        self.cur_env = None

    def next_level(self):
        self.stop_level()
        self.start_level()

    def objects_to_numpy(objs):
        width, height = self.out_size
        surface = cairo.ImageSurface(cairo.FORMAT_A8, width, height)
        cr = cairo.Context(surface)
        cr.scale(*(1/self.scale))

        cr.rectangle(*corners_to_rectangle(self.corners))
        cr.set_source_rgb(0, 0, 0)
        cr.fill()

        for obj in objs: obj.draw(cr, self.corners)

        data = surface.get_data()
        data = np.array(data, dtype = float)/255
        data = data.reshape([height, surface.get_stride()])
        data = data[:,:width]
        return data

    def get_state(self):

        ori_layer = objects_to_numpy(self.env.objs[self.env.min_objs:])
        all_layer = objects_to_numpy(self.env.objs)
        goal_layer = objects_to_numpy(self.env.cur_goal())
        if self.tool == -1: selected_objs = ()
        else: selected_objs = self.tools[self.tool].get_highlighted(self.env)
        sel_layer = objects_to_numpy(selected_objs)

        return np.stack((ori_layer, all_layer, goal_layer, sel_layer), axis = -1)

    def action_set_tool(self, tool_index):
        assert(tool is None)
        assert(tool_index >= 0
               and tool_index < len(self.tools)
               and self.tool_mask[tool_index])
        self.tool = tool_index
        self.tools[tool_index].initialize()

    def action_click(self, x, y, auto_proceed = True):
        coor = np.array(x,y)*self.scale
        tool_status = self.tool.run(self.env, coor, 1)
        if tool_status is None: return 0, False

        finish = False
        reward = 0
        if tool_status is False: reward -= 0.1
        else:
            num_outs = len(self.env.steps[-1].otypes)
            tool_output = self.env.objs[-num_outs:]
            rem_goals_next = []
            for goal in self.remaining_goals:
                if any(goal.identical_to(out) for out in tool_output):
                    reward += self.goal_reward
                else: rem_goals_next.append(self.remaining_goals)
            self.remaining_goals = rem_goals_next
            if not self.remaining_goals: finish = True
            
        self.moves += 1
        if self.moves == self.max_moves: finish = True
        elif self.drop_prob > 0 and self.drop_prob > np.random.random(): finish = True

        if finish and auto_restart: self.next_level()

        return reward, finish
