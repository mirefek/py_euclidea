from constructions import *

def init(env):
    A = env.add_free(284.0, 187.0)
    B = env.add_free(441.0, 248.0)
    l = env.add_free_line((0.5, 270.0), (634.0, 327.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, l)

def construct_goals(A, B, l):
    A2 = reflect_by_line(A, l)
    X = intersection_tool(line_tool(B, A2), l)
    return (segment_tool(X,A), segment_tool(X,B))

def additional_bb(A,B,l, goal):
    X = min((A,B), key = lambda X: l.dist_from(X.a))
    return reflect_by_line(X, l)

def ini_check(A,B,l, goal, scale):
    ddistA = np.dot(l.n, A.a)
    ddistB = np.dot(l.n, B.a)
    return (ddistA-l.c) * (ddistB-l.c) > 0
