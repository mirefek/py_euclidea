from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (217.0, 290.0), (352.5, 290.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(A, B)

def construct_goals(A, B):
    result = []
    n_base = vector_perp_rot(A.a - B.a)
    for X,Y in (A,B), (B,A):
        X = X.a
        Y = Y.a
        for n in -n_base, n_base:
            v = Y-X
            d = (v+n)/np.sqrt(2)
            result.append((
                Segment(X, X+d),
                Segment(X+d, Y+d),
                Segment(Y+d, Y),
            ))
    return result
