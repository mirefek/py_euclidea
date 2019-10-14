from constructions import *

def init(env):
    circ = env.add_free_circ((329.0, 247.0), 118.6, hidden_center = False)
    X = env.add_free(279.0, 196.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(circ, X)

def construct_goals(circ, X):
    n = circ.c - X.a
    line = Line(n, np.dot(n, X.a))
    A,B = intersection_lc(line, circ)
    return Segment(A, B)
