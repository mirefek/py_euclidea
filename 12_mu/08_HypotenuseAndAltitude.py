from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (197.5, 309.0), (443.5, 309.0))
    X,Y,_ = env.add_free_segment(
        (430.5, 136.5), (465.5, 223.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,X,Y)

def construct_goals(A,B,X,Y):
    h_base = np.linalg.norm(Y.a-X.a)
    circ = circle_by_diameter(A,B)
    result = []
    for h in -h_base, h_base:
        l = line_tool(A, B)
        l.c += h
        for C in intersection_tool(circ, l):
            result.append((segment_tool(A, C), segment_tool(B, C)))
    return result
