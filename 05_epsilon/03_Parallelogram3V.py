from constructions import *

def init(env):
    A = env.add_free(299.5, 194.5)
    B = env.add_free(238.0, 285.0)
    C = env.add_free(383.0, 284.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(A, B, C)

def construct_goals(A, B, C):
    D, *segments = parallelogram(A, B, C)
    return segments
