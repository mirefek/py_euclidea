from constructions import *

def init(env):
    A,B,seg = env.add_free_segment(
        (181.0, 255.0), (493.5, 256.5))
    C = env.add_dep((277.0, 255.5), seg)
    D = env.add_free(542.5, 6.5, hidden = True)
    ray = env.add_ray(C, D)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C, ray)

def construct_goals(A, B, C, ray):
    a = np.linalg.norm(A.a - C.a)
    b = np.linalg.norm(B.a - C.a)
    c = 2*a*b/(a+b)
    return Point(ray.start_point + c*ray.v)
