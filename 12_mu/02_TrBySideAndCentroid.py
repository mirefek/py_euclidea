from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (205.5, 359.0), (490.0, 355.5))
    G = env.add_free(316.0, 287.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,G)

def construct_goals(A,B,G):
    C = Point(3*G.a-A.a-B.a)
    return (segment_tool(A,C), segment_tool(B,C))
