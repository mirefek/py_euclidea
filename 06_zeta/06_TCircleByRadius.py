from constructions import *

def seg_init():
    X = random_point()
    Y = random_point()
    v = vector_perp_rot(X-Y)
    return X+v, Y+v

def init(env):
    A = env.add_free(216.0, 249.5, rand_init = False)
    B = env.add_free(280.5, 165.5, rand_init = False)
    env.add_segment(A,B)
    env.add_rand_init((A,B), seg_init)
    C = env.add_free(390.0, 268.5)

    env.set_tools("compass")
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    return compass_tool(A,B,C)
