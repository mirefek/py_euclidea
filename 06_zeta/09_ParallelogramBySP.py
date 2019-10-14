from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (173.5, 306.0), (386.0, 305.5))
    M = env.add_free(367.0, 174.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,M)

def construct_goals(A,B,M):
    v = (B.a-A.a)/2
    C = Point(M.a+v)
    D = Point(M.a-v)
    return (
        segment_tool(B,C),
        segment_tool(C,D),
        segment_tool(D,A),
    )
