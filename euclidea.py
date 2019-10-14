#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import cairo
from constructions import *
from tools import MoveTool, key_to_tool, tool_name_to_key

from environment import ConstrStep, MovableStep, load_level

class Drawing(Gtk.Window):

    def __init__(self, env, win_size):
        super(Drawing, self).__init__()
        self.shift = np.array([0,0])
        self.scale = 1
        self.mb_grasp = None

        self.set_env(env)
        self.darea = Gtk.DrawingArea()
        self.darea.connect("draw", self.on_draw)
        self.darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK |
                              Gdk.EventMask.KEY_PRESS_MASK |
                              Gdk.EventMask.SCROLL_MASK |
                              Gdk.EventMask.BUTTON1_MOTION_MASK |
                              Gdk.EventMask.BUTTON2_MOTION_MASK )
        self.add(self.darea)

        self.darea.connect("button-press-event", self.on_button_press)
        self.darea.connect("scroll-event", self.on_scroll)
        self.darea.connect("motion-notify-event", self.on_motion)
        self.connect("key-press-event", self.on_key_press)

        self.set_title("Drawing")
        self.resize(*win_size)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def set_env(self, env):
        self.env = env
        print("Enabled tools:")
        for name in sorted(self.env.enabled_tools):
            if name not in tool_name_to_key:
                print(name)
            key = tool_name_to_key[name]
            print("  {} ({})".format(name, key))
        assert(env.start_tool in env.enabled_tools)
        self.set_tool(tool_name_to_key[env.start_tool])

    def get_coor(self, e):
        return np.array([e.x, e.y])/self.scale - self.shift
        
    def on_scroll(self,w,e):
        coor = self.get_coor(e)
        if e.direction == Gdk.ScrollDirection.DOWN: self.scale *= 0.9
        elif e.direction == Gdk.ScrollDirection.UP: self.scale /= 0.9
        print("zoom {}".format(self.scale))
        self.shift = np.array([e.x, e.y])/self.scale - coor
        self.darea.queue_draw()

    def on_motion(self,w,e):
        if e.state & Gdk.ModifierType.BUTTON1_MASK:
            if isinstance(self.tool, MoveTool) and self.tool.grabbed is not None:
                step = self.tool.grabbed
                step.coor = self.get_coor(e)
                self.env.run_steps()
                self.tool.refresh(self.env)
                self.darea.queue_draw()
        if e.state & Gdk.ModifierType.BUTTON2_MASK:
            if self.mb_grasp is None: return
            self.shift = np.array([e.x, e.y])/self.scale - self.mb_grasp
            self.darea.queue_draw()

    def on_draw(self, wid, cr):

        corners = np.array([
            [0, 0],
            [self.darea.get_allocated_width(), self.darea.get_allocated_height()],
        ])/self.scale - self.shift
        cr.scale(self.scale, self.scale)
        cr.translate(*self.shift)
        cr.rectangle(*corners_to_rectangle(corners))
        cr.set_source_rgb(1, 1, 1)
        cr.fill()

        highlighted = self.tool.get_highlighted(self.env)
        goals = self.env.cur_goal()
        constructed = tuple(self.env.objs_of_type(GeoObject))
        constr_basic = []
        constr_desired = []
        for obj in constructed:
            if any(goal.identical_to(obj) for goal in goals):
                constr_desired.append(obj)
            else:
                constr_basic.append(obj)
        goals_remaining = [
            goal for goal in goals
            if not any(goal.identical_to(obj) for obj in constr_desired)
        ]

        for t in (PointSet, Point):
            for objs, color in (
                    (goals_remaining, (0.87, 0.86, 0.2)),
                    (constr_basic, (0, 0, 0)),
                    (constr_desired, (0.06, 0.58, 0.07)),
                    (highlighted, (0.7, 0, 1)),
            ):
                
                cr.set_source_rgb(*color)
                for obj in objs:
                    if isinstance(obj, t): obj.draw(cr, corners, self.scale)

    def on_key_press(self,w,e):

        keyval = e.keyval
        keyval_name = Gdk.keyval_name(keyval)
        #print(keyval_name)
        if keyval_name in key_to_tool:
            self.set_tool(keyval_name)
            self.darea.queue_draw()
        #elif keyval_name == 'd':
        #    self.tool = self.dep_point_tool
        #    print("Dependent point tool")
        #    self.tool_data = []
        #elif keyval_name == 'm':
        #    self.tool = self.move_tool
        #    print("Move tool")
        #    self.tool_data = None
        #elif keyval_name == 'h':
        #    self.tool = self.hide_tool
        #    print("Hide tool")
        #    self.tool_data = None
        elif keyval_name == 'r':
            print("Random")
            self.env.rnd_init()
            self.darea.queue_draw()
        elif keyval_name == 'BackSpace':
            print("BACK")
            self.env.pop()
            self.tool.refresh(self.env)
            print("Status:", env.check_goal())
            self.darea.queue_draw()
        elif keyval_name == "Tab":
            self.env.next_goal()
            self.darea.queue_draw()
        elif keyval_name == "Escape":
            Gtk.main_quit()
        else:
            return False

    def set_tool(self, key):
        tool, name = key_to_tool[key]
        if name not in self.env.enabled_tools:
            print("tool {} is not enabled on the current problem".format(name))
            return
        self.tool = tool
        print("Tool: {}".format(name))
        self.tool.initialize(self.env)

    def on_button_press(self, w, e):

        coor = self.get_coor(e)
        if e.button == 1 and self.tool is not None:
            if e.type != Gdk.EventType.BUTTON_PRESS: return
            tool_status = self.tool.run(self.env, coor, self.scale)
            if tool_status is True:
                print("Game status:", env.check_goal())
            elif tool_status is False:
                print("Tool failed")
            self.darea.queue_draw()
        if e.button == 2:
            self.mb_grasp = coor

if __name__ == "__main__":
    np.random.seed(2442432778)

    import argparse
    cmd_parser = argparse.ArgumentParser(prog='euclidea.py')
    cmd_parser.add_argument("fname", type=str,
                            help="problem filename")
    config = cmd_parser.parse_args()

    fname = config.fname
    assert(fname.endswith(".py"))
    level_pack, level = fname[:-3].split('/')
    win_size = 637, 490
    #win_size = 512, 512
    env = load_level(level_pack, level, win_size)

    #env = load_level("01_alpha", "01_T1_line")
    #env = load_level("01_alpha", "02_T2_circle")
    #env = load_level("01_alpha", "03_T3_point")
    #env = load_level("01_alpha", "04_TIntersect")
    #env = load_level("01_alpha", "05_TEquilateral")
    #env = load_level("01_alpha", "06_Angle60")
    #env = load_level("01_alpha", "07_PerpBisector")
    #env = load_level("01_alpha", "08_TPerpBisector")
    #env = load_level("01_alpha", "09_Midpoint")
    #env = load_level("01_alpha", "10_CircleInSquare")
    #env = load_level("01_alpha", "11_RhombusInRect")
    #env = load_level("01_alpha", "12_CircleCenter")
    #env = load_level("01_alpha", "13_SquareInCircle")
    win = Drawing(env, win_size)
    Gtk.main()
