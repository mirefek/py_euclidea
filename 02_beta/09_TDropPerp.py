from constructions import *

def init(env):
    X = env.add_free(318.5, 126.0)
    l = env.add_free_line((5.5, 253.5), (625.0, 253.5))

    env.set_tools(
        "perpendicular",
    )
    env.goal_params(X, l)

def construct_goals(X, l):
    return perp_tool(l, X)

def additional_bb(X, l, goal):
    return intersection_tool(l, goal)
