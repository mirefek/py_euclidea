from constructions import *

def init(env):
    A = env.add_free(263.5, 285.0)
    B = env.add_free(399.0, 220.5)

    env.set_tools(
        "move", "point", "circle", "intersection",
    )
    env.goal_params(A, B)

def construct_goals(A, B):
    return midpoint_tool(A, B)

def additional_bb(A, B, goal):
    v = A.a - B.a
    n = vector_perp_rot(v)
    result = A.a-v, A.a+n, A.a-n, B.a+v, B.a+n, B.a-n
    return [ Point(coor) for coor in result ]
