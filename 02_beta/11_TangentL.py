from constructions import *

def init(env):
    C = env.add_free(350.0, 235.0)
    l = env.add_free_line((1.0, 340.0), (634.5, 331.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(C, l)

def construct_goals(C, l):
    r = l.dist_from(C.a)
    return Circle(C.a, r)
