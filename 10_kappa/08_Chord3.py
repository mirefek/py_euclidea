from constructions import *

def init(env):
    C = env.add_free(333.5, 255.5)
    X = env.add_free(281.0, 327.5, hidden = True)
    A = env.add_free(206.0, 337.5)
    c1 = env.add_circle(C, X)
    c2 = env.add_circle(C, A)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(C, c1, c2, A)

def construct_goals(C, c1, c2, A):
    c3 = Circle(2*c1.c - A.a, 2*c1.r)
    result = []
    for B in reversed(intersection_tool(c1, c3)):
        result.append((
            segment_tool(*intersection_tool(c2, line_tool(A,B))),
        ))
    return result
