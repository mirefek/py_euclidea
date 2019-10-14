from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (237.0, 346.5), (433.5, 346.5))
    A2,B2,_ = env.add_free_segment(
        (218.5, 209.5), (284.0, 124.0))
    A3,B3,_ = env.add_free_segment(
        (491.0, 98.5), (491.5, 227.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,A2,B2,A3,B3)

def construct_goals(A,B,A2,B2,A3,B3):
    result = []
    for X,Y in (A,B),(B,A):
        c2 = compass_tool(A2,B2,X)
        c3 = compass_tool(A3,B3,Y)
        for C in intersection_tool(c2,c3):
            result.append((
                segment_tool(X,C),
                segment_tool(Y,C),
            ))
    return result

def ini_check(A,B,A2,B2,A3,B3,goal,scale):
    tri_segments = list(goal)+[segment_tool(A,B)]
    segments = [
        segment_tool(A2,B2),
        segment_tool(A3,B3),
    ]
    if is_intersecting_ll(*segments): return False
    for s1 in tri_segments:
        for s2 in segments:
            if is_intersecting_ll(s1, s2):
                return False
    return True
