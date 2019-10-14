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
    env.goal_params(A,B,C,D, a,b,c,d)

def construct_goals(A,B,C,D, a,b,c,d):
    X = intersection_tool(line_tool(A,C), line_tool(B,D))
    line = parallel_tool(a, X)
    return segment_tool(
        intersection_tool(line, b),
        intersection_tool(line, d),
    )
