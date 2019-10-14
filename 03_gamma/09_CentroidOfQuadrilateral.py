from constructions import *

def init(env):
    A = env.add_free(242.0, 168.5, rand_init = False)
    B = env.add_free(370.0, 188.0, rand_init = False)
    C = env.add_free(482.0, 354.0, rand_init = False)
    D = env.add_free(159.0, 354.0, rand_init = False)
    env.add_rand_init((A,B,C,D), random_convex_quadrilateral)
    for (X,Y) in (A,B),(B,C),(C,D),(D,A):
        env.add_segment(X,Y)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(A,B,C,D)

def construct_goals(A,B,C,D):
    return Point((A.a+B.a+C.a+D.a)/4)
