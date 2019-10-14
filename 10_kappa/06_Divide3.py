from constructions import *

def init(env):
    A,B,_ = env.add_free_segment((246.5, 237.0), (409.5, 237.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B)

def construct_goals(A,B):
    return Point((2*A.a+B.a)/3), Point((A.a+2*B.a)/3)
