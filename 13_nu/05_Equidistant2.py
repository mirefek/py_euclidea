from constructions import *

def init(env):
    B, ray1, ray2 = env.add_free_angle(
        (156.5, 293.5), (568.0, 25.5), (615.5, 310.0))
    M = env.add_free(374.5, 238.5, rand_init = False)
    env.add_rand_init(M, random_point_in_angle, (ray1, ray2))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(B, ray1, ray2, M)

def construct_goals(B, ray1, ray2, M):
    ratio = np.abs(np.dot(ray1.v, ray2.n))
    ap_center = B.a * ratio**2 / (ratio**2 - 1) + M.a / (1 - ratio**2)
    ap_radius = B.dist_from(M.a) * abs(ratio / (ratio**2 - 1))
    apollonius_circ = Circle(ap_center, ap_radius)
    result = []
    for X in reversed(intersection_tool(ray2, apollonius_circ)):
        if X is None: continue
        Y = Point(ray1.closest_on(X.a))
        result.append((segment_tool(X,Y), segment_tool(X,M)))
    return result
