from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (169.0, 250.0), (270.5, 136.0))
    C = env.add_free(320.0, 239.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    A2 = Point(2*C.a-A.a)
    B2 = Point(2*C.a-B.a)
    return (
        A2, B2, segment_tool(A2, B2)
    )
