from constructions import *

def init(env):
    A,B,seg = env.add_free_segment(
        (226.0, 285.5), (439.5, 285.5))
    C = env.add_dep((290.0, 285.5), seg)
    X = env.add_free(632.0, 111.5, hidden = True)
    ray = env.add_ray(C, X)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C,ray)

def construct_goals(A,B,C,ray):
    a = C.dist_from(A.a)
    b = C.dist_from(B.a)
    c = np.sqrt(a*b)
    return Point(ray.start_point + c * ray.v)
