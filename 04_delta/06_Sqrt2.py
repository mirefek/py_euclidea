from constructions import *

def init(env):
    A = env.add_free(238.5, 256.0)
    B = env.add_free(355.0, 255.5)
    env.add_ray(A, B)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(A, B)

def construct_goals(A, B):
    coef = np.sqrt(2)
    return Point(coef*B.a + (1-coef)*A.a)
