from constructions import *

def init(env):
    A = env.add_free(207.5, 258.5)
    B = env.add_free(390.5, 257.0)
    ray = env.add_ray(A,B)
    C = env.add_dep((499.5, 256.0), ray)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C,ray)

def construct_goals(A,B,C,ray):
    v = ray.v
    return Point(A.a + v*(np.dot(B.a-A.a,v)**2 / np.dot(C.a-A.a,v)))
