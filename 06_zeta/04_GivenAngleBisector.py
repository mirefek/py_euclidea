from constructions import *

def init(env):
    A = env.add_free(254.5, 173.5)
    B = env.add_free(376.0, 324.0)
    l = env.add_free_line((27.0, 274.0), (621.5, 269.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(A, B, l)

def construct_goals(A, B, l):
    A2 = reflect_by_line(A, l)
    X = intersection_tool(line_tool(B, A2), l)
    return (ray_tool(X,A), ray_tool(X,B))

def ini_check(A,B,l, goal, scale):
    ddistA = np.dot(l.n, A.a)
    ddistB = np.dot(l.n, B.a)
    return (ddistA-l.c) * (ddistB-l.c) < 0
