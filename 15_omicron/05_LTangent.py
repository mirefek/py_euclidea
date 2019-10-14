from constructions import *

def init(env):
    circ = env.add_free_circ((370.5, 247.0), 113.0)
    A = env.add_free(167.0, 276.0)

    env.set_tools(
        "move", "point", "line", "intersection",
    )
    env.goal_params(circ, A)

def construct_goals(circ, A):
    C = Point(circ.c)
    return [
        (line_tool(A,X),)
        for X in intersection_tool(circ, circle_by_diameter(A,C))
    ]
