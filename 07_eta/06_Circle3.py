from constructions import *

def init(env):
    A = env.add_free(214.5, 154.0)
    B = env.add_free(453.5, 216.0)
    C = env.add_free(295.5, 351.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C)

def construct_goals(A, B, C):
    return circumcircle_tool(A, B, C)
