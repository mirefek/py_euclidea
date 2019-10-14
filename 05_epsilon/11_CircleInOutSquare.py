from constructions import *

def init(env):
    (A,B,C,D),_ = env.add_free_square(
        (229.5, 322.0), (408.5, 322.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(A,B,C,D)

def construct_goals(A,B,C,D):
    X = midpoint_tool(C,D)
    return circumcircle_tool(X,A,B)
