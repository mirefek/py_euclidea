from constructions import *
from environment import ConstrStep, MovableStep
import itertools

class Tool:
    def initialize(self, env):
        self.refresh(env)
    def run(self, env, coor, scale):
        raise NotImplemented
    def get_highlighted(self, env):
        return []
    def refresh(self, env):
        pass

class MoveTool(Tool):
    def initialize(self, env):

        self.grabbed = None
        self.refresh(env)

    def get_highlighted(self, env):
        return self.movable
    def refresh(self, env):
        self.movable = []
        for step in env.steps:
            if isinstance(step, MovableStep):
                i, = step.output
                if env.objs[i] is not None: self.movable.append(env.objs[i])

    def run(self, env, coor, scale):
        if not self.movable:
            self.grabbed = None
            return
        dist, obj = min((obj.dist_from(coor)*scale, obj) for obj in self.movable)
        if dist > 20:
            self.grabbed = None
            return
        for step in env.steps:
            if obj.index in step.output:
                assert(isinstance(step, MovableStep))
                self.grabbed = step
                break
        else: raise Exception("Movable step not found")

class StdTool(Tool):
    def __init__(self, tool_f, in_types, out_type):
        self.tool_f = tool_f
        self.in_types = in_types
        self.out_type = out_type
    def refresh(self, env):
        self.args = []
    def get_highlighted(self, env):
        return [env.objs[i] for i in self.args]
    def get_out_types(self, *args):
        return self.out_type,
    def run(self, env, coor, scale):
        obj_type = self.in_types[len(self.args)]
        dist, obj = env.closest_obj_of_type(coor, obj_type)
        dist *= scale
        if obj is None or dist > 20:
            self.args = []
            return False
        self.args.append(obj.index)
        if len(self.args) == len(self.in_types):
            step = ConstrStep(self.tool_f, tuple(self.args), self.get_out_types(env, self.args))
            self.args = []
            return env.add_and_run(step)

class IntersectionTool(StdTool):
    def __init__(self):
        StdTool.__init__(self, intersection_tool, (PointSet, PointSet), None)
    def get_out_types(self, env, args):
        if any(isinstance(env.objs[i], Circle) for i in args):
            return Point, Point
        else: return Point

class PointTool(Tool):
    def run(self, env, coor, scale):
        max_dist = 20
        objs = list(filter(
            lambda obj: obj.dist_from(coor)*scale < max_dist,
            env.objs_of_type(PointSet)
        ))
        intersections = []
        for obj0, obj1 in itertools.combinations(objs, 2):
            try:
                for point in singleton_to_tuple(intersection_tool(obj0, obj1)):
                    if point is None: continue
                    dist = point.dist_from(coor)*scale
                    if dist < max_dist:
                        intersections.append((dist, obj0.index, obj1.index))
            except:
                pass
        if len(intersections) > 0:
            dist, obj0, obj1 = min(intersections, key = lambda x: x[0])
            step = MovableStep(intersection_close_to, coor, (obj0, obj1), Point)
        elif len(objs) > 0:
            obj = min(objs, key = lambda obj: obj.dist_from(coor))
            step = MovableStep(point_on, coor, (obj.index,), Point)
        else:
            step = MovableStep(Point, coor, (), Point)
        return env.add_and_run(step)

key_to_tool = {
    'm' : (MoveTool(), 'move'),
    'x' : (PointTool(), 'point'),
    'l' : (StdTool(line_tool, (Point, Point), Line), 'line'),
    'c' : (StdTool(circle_tool, (Point, Point), Circle), 'circle'),
    'b' : (StdTool(perp_bisector_tool, (Point, Point), Line), 'perp_bisector'),
    'a' : (StdTool(angle_bisector_tool, (Point, Point, Point), Line), 'angle_bisector'),
    't' : (StdTool(perp_tool, (Line, Point), Line), 'perpendicular'),
    'h' : (StdTool(parallel_tool, (Line, Point), Line), 'parallel'),
    'g' : (StdTool(compass_tool, (Point, Point, Point), Circle), 'compass'),
    'i' : (IntersectionTool(), 'intersection'),
}
tool_name_to_key = dict((name, key) for (key, (tool, name)) in key_to_tool.items())
