from constructions import *

def init(env):
    A = env.add_free(280.5, 114.5)
    C = env.add_free(328.0, 277.0)
    X = env.add_free(440.5, 277.0, hidden = True)
    env.add_circle(C, X)
    l = env.add_line(C, X)

    env.set_tools(
        "move", "point", "line", "intersection",
    )
    env.goal_params(A, l)

def construct_goals(A, l):
    return Point(l.closest_on(A.a))
