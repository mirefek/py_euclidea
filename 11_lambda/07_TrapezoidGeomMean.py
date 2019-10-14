from constructions import *

def init(env):
    (A,B,C,D),(a,b,c,d) = env.add_free_trapezoid(
        (478.0, 331.5), (181.5, 331.5), (268.5, 161.5), (412.0, 161.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C,D)

def construct_goals(A,B,C,D):
    la = A.dist_from(B.a)
    lb = C.dist_from(D.a)
    lc = np.sqrt(la*lb)
    coef = (lc-lb) / (la-lb)
    return Segment(A.a*coef + D.a*(1-coef), B.a*coef + C.a*(1-coef))
