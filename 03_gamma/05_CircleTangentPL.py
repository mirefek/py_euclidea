from constructions import *

def init(env):
    A = env.add_free(249.5, 227.0)
    B = env.add_free(348.5, 340.5)
    L = env.add_free(8.0, 340.0, hidden = True)
    l = env.add_line(B, L)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(A, B, l)

def construct_goals(A, B, l):
    b = perp_bisector_tool(A, B)
    p = perp_tool(l, B)
    C = intersection_tool(p, b)
    return circle_tool(C, B)
