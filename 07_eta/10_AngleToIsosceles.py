from constructions import *

def init(env):
    A,ray1,ray2 = env.add_free_angle(
        (166.0, 332.0), (493.0, 6.0), (621.5, 332.0))
    B = env.add_free(377.5, 180.5, rand_init = False)
    env.add_rand_init(B, random_point_in_angle, (ray1, ray2))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(ray1,ray2,B)

def construct_goals(ray1, ray2, B):
    if np.dot(ray1.v, ray2.v) >= 0: n = ray1.v + ray2.v
    else: n = vector_perp_rot(ray1.v - ray2.v)
    l = Line(n, np.dot(n, B.a))
    X = intersection_ll(l, ray1)
    Y = intersection_ll(l, ray2)

    return Segment(X,Y)
