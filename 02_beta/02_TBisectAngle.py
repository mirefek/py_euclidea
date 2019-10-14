from constructions import *

def init(env):
    A = env.add_free(175.5, 315.0)
    X = env.add_free(259.5, 196.6)
    Y = env.add_free(349.9, 317.0)
    env.add_ray(A, X)
    env.add_ray(A, Y)
    env.set_tools(
        "angle_bisector",
    )
    env.goal_params(A, X, Y)

def construct_goals(A, X, Y):
    return angle_bisector_tool(X, A, Y)
