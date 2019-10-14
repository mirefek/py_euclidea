from constructions import *

def init(env):
    A = env.add_free(232.0, 251.0)
    B = env.add_free(351.5, 250.0)

    env.set_tools(
        "move", "point", "circle",
        "intersection",
    )
    env.goal_params(A, B)

def construct_goals(A, B):
    return [
        (Point(2*B.a - A.a),),
        (Point(-2*B.a + 3*A.a),),
    ]
