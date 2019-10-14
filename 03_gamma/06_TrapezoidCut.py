from constructions import *

def init(env):
    (A,B,C,D),_ = env.add_free_trapezoid(
        (477.5, 331.5), (181.5, 331.5), (269.0, 213.0), (432.0, 213.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(A, B, C, D)

def construct_goals(A, B, C, D):
    X = (A.a+B.a)/2
    Y = (C.a+D.a)/2
    return Segment(X, Y)
