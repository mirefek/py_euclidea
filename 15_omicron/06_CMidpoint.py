from constructions import *

def init(env):
    circ = env.add_free_circ((312.5, 252.1), 113.5)

    env.set_tools(
        "move", "point", "circle",
        "compass", "intersection",
    )
    env.goal_params(circ)

def construct_goals(circ):
    return Point(circ.c)
