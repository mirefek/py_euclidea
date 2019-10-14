from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (220.5, 237.0), (428.5, 236.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B)

def construct_goals(A, B):
    return (
        (Point((5*A.a+B.a)/6),),
        (Point((A.a+5*B.a)/6),),
    )
