from constructions import *

def init(env):
    X = env.add_free(231.0, 206.5)
    Y = env.add_free(396.5, 205.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(X, Y)

def construct_goals(X, Y):
    X = X.a
    Y = Y.a
    v1 = (Y-X)/2
    result = []
    for v2 in -vector_perp_rot(v1), vector_perp_rot(v1):
        A = X+v1-v2
        B = Y+v1+v2
        C = Y+3*v2-v1
        D = X+v2-v1
        result.append((
            Segment(A, B),
            Segment(B, C),
            Segment(C, D),
            Segment(D, A),
        ))
    return result
