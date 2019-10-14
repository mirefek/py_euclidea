from constructions import *

def init(env):
    A = env.add_free(166.0, 269.0)
    circ = env.add_free_circ(
        (383.0, 245.5), 79.85, hidden_center = False)

    env.set_tools(
        "move", "point", "circle",
        "compass", "intersection",
    )
    env.goal_params(A, circ)

def construct_goals(A, circ):
    return intersection_tool(
        line_tool(A, Point(circ.c)),
        circ,
    )
