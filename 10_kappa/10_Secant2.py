from constructions import *

def init(env):
    circ = env.add_free_circ((359.5, 256.0), 100.4, hidden_center = False)
    A = env.add_free(171.0, 298.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(circ, A)

def construct_goals(circ, A):
    circ2 = Circle(2*circ.c - A.a, 2*circ.r)
    return [
        (segment_tool(A, X),)
        for X in reversed(intersection_tool(circ, circ2))
    ]

def ini_check(circ, A, goal, scale):
    return circ.dist_from(A.a) > 20/scale
