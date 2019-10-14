from constructions import *

def init(env):
    A = env.add_free(143.5, 322.5)
    X = env.add_free(358.0, 124.0)
    Y = env.add_free(473.0, 323.5)
    env.add_segment(A,X)
    env.add_segment(A,Y)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,X,Y)

def construct_goals(A,X,Y):
    v1 = A.a-X.a
    v2 = Y.a-A.a
    v1 /= np.linalg.norm(v1)
    v2 /= np.linalg.norm(v2)
    v = v1+v2
    ratio = np.linalg.norm(v)
    ap_center = Y.a * ratio**2 / (ratio**2 - 1) + X.a / (1 - ratio**2)
    ap_radius = Y.dist_from(X.a) * abs(ratio / (ratio**2 - 1))
    apollonius_circ = Circle(ap_center, ap_radius)
    path = Ray(X.a, v)
    x = intersection_close_to(
        X.a,
        apollonius_circ, path,
    ).dist_from(Y.a)
    return Segment(X.a + x*v1, Y.a - x*v2)

def ini_check(A,X,Y, goal,scale):
    if not segment_tool(A, X).contains(goal.end_points[0]): return False
    if not segment_tool(A, Y).contains(goal.end_points[1]): return False
    return True
