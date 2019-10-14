from constructions import *

def init(env):
    X = env.add_free(263.5, 313.0)
    Y = env.add_free(404.5, 181.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(X, Y)

def construct_goals(X, Y):
    X = X.a
    Y = Y.a
    v = vector_perp_rot(X-Y)/2
    A = X + v
    B = Y + v
    C = Y - v
    D = X - v
    return (
        Segment(A, B),
        Segment(B, C),
        Segment(C, D),
        Segment(D, A),
    )
