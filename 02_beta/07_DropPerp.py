from constructions import *

def init(env):
    X = env.add_free(318.5, 126.0)
    l = env.add_free_line((9.0, 273.0), (636.0, 273.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "intersection",
    )
    env.goal_params(X, l)

def construct_goals(X, l):
    return perp_tool(l, X)

def additional_bb(X, l, goal):
    return intersection_tool(l, goal)
