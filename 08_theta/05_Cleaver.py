from constructions import *

def init(env):
    (A,B,C),_ = env.add_free_triangle(
        (242.0, 175.0), (172.0, 341.5), (466.0, 341.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C)

def construct_goals(A_in, B_in, C_in):
    result = []
    for (A,B,C) in rots_args(A_in, B_in, C_in):
        M = midpoint_tool(B,C)
        dir_line = angle_bisector_tool(B,A,C)
        result.append((parallel_tool(dir_line, M),))
    return result
