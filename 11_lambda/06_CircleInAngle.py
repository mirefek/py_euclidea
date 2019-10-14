from constructions import *

def init(env):
    A, ray1, ray2 = env.add_free_angle(
        (123.0, 326.5), (560.5, 19.0), (619.5, 391.0))
    X = env.add_free(383.5, 208.5, rand_init = None)
    env.add_rand_init(X, random_point_in_angle, (ray1, ray2))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, ray1, ray2, X)

def construct_goals(A, ray1, ray2, X):
    C0 = A.a + 100*(ray1.v + ray2.v)
    r0 = ray1.dist_from(C0)
    result = []
    for X0 in intersection_tool(Circle(C0, r0), line_tool(A, X)):
        ratio = np.linalg.norm(X.a-A.a) / np.linalg.norm(X0.a-A.a)
        result.append((Circle(C0*ratio + A.a*(1-ratio), r0*ratio),))
    return result
