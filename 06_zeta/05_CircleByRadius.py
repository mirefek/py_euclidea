from constructions import *

def seg_init():
    X = random_point()
    Y = random_point()
    v = vector_perp_rot(X-Y)
    return X+v, Y+v

def init(env):
    A = env.add_free(177.5, 249.0, rand_init = False)
    B = env.add_free(242.5, 165.5, rand_init = False)
    env.add_segment(A,B)
    env.add_rand_init((A,B), seg_init)
    C = env.add_free(447.0, 268.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    return compass_tool(A,B,C)
