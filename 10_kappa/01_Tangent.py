from constructions import *

def init(env):
    circ = env.add_free_circ((370.0, 247.0), 112.55, hidden_center = False)
    A = env.add_free(167.0, 276.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(circ, A)

def construct_goals(circ, A):
    C = Point(circ.c)
    return [
        (line_tool(A,X),)
        for X in intersection_tool(circ, circle_by_diameter(A,C))
    ]
