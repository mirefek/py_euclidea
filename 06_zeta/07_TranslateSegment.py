from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (227.5, 260.5), (312.0, 174.5))
    C = env.add_free(362.0, 277.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    result = []
    v_base = B.a-A.a
    for v in v_base, -v_base:
        D = Point(C.a + v)
        result.append((D, segment_tool(C,D)))
    return result
