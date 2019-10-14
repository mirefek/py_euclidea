from constructions import *

def init(env):
    (A,B,C),_ = env.add_free_triangle(
        (274.0, 137.0), (159.0, 341.5), (479.0, 341.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    return [
        (segment_tool(midpoint_tool(X,Y), midpoint_tool(X,Z)),)
        for (X,Y,Z) in rots_args(A,B,C)
    ]
