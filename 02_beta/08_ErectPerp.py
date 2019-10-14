from constructions import *

def init(env):
    X = env.add_free(339.0, 276.0)
    Y = env.add_free(2.0, 277.5, hidden = True)
    l = env.add_line(X, Y)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "intersection",
    )
    env.goal_params(X, l)

def construct_goals(X, l):
    return perp_tool(l, X)
