from constructions import *

def init(env):
    A = env.add_free(406.5, 314.5)
    B = env.add_free(232.0, 311.5)
    C = env.add_free(340.5, 158.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    return [
        (line_tool(midpoint_tool(X,Y), midpoint_tool(X,Z)), )
        for (X,Y,Z) in ((A,B,C), (B,C,A), (C,A,B))
    ]
