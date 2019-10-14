from constructions import *

def init(env):
    circ = env.add_free_circ((319.5, 245.0), 119.6, hidden_center = False)
    A = env.add_free(153.0, 226.5)
    B = env.add_free(489.5, 201.0)

    env.set_tools(
        "move", "point", "circle",
        "compass", "intersection",
    )
    env.goal_params(circ, A, B)

def construct_goals(circ, A, B):
    return intersection_tool(line_tool(A, B), circ)

def additional_bb(circ, A, B, goal):
    return reflect_by_line(Point(circ.c), line_tool(A, B))
