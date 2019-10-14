from constructions import *

def init(env):
    C = env.add_free(267.5, 174.5)
    X = env.add_free(426.0, 258.0)
    Y = env.add_free(327.5, 316.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(C, X, Y)

def construct_goals(C, X, Y):
    D = Point(C.a + Y.a - X.a)
    return line_tool(C, D)
