from constructions import *

def init(env):
    O = env.add_free(210.0, 294.0)
    A = env.add_free(354.5, 292.5)
    l = env.add_line(O, A)
    ray_l = env.add_ray(O, A, hidden = True)
    B = env.add_dep((452.0, 291.0), ray_l)
    C = env.add_free(283.0, 224.0)
    ray = env.add_ray(O,C)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(O,A,B,C,ray)

def construct_goals(O,A,B,C,ray):
    d = O.dist_from(B.a) * O.dist_from(C.a) / O.dist_from(A.a)
    return Point(ray.start_point + d * ray.v)
