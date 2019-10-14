from constructions import *

def init(env):
    C = env.add_free(322.0, 253.5)
    X = env.add_free(420.5, 215.5)
    env.add_circle(C, X)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(C, X)

def construct_goals(C, X):
    n = C.a - X.a
    return Line(n, np.dot(n, X.a))
