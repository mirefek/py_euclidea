from constructions import *

def init(env):
    X = env.add_free(303.5, 210.0)
    l = env.add_free_line((2.0, 298.0), (630.5, 306.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(l, X)

def construct_goals(l, X):
    return parallel_tool(l, X)

def additional_bb(l, X, goal):
    return Point(l.closest_on(X.a))
