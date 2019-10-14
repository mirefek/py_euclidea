from constructions import *

def init(env):
    circ = env.add_free_circ((312.75, 251.75), 113.75)
    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "intersection",
    )
    env.goal_params(circ)

def construct_goals(circ):
    return Point(circ.c)
