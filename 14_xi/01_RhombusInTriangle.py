from constructions import *

def init(env):
    (A,B,C),(a,b,c) = env.add_free_triangle(
        (200.5, 311.0), (296.5, 127.5), (491.5, 314.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C,a,b,c)

def construct_goals(A,B,C,a,b,c):
    Y = intersection_tool(
        angle_bisector_tool(B,A,C),
        a,
    )
    X = intersection_tool(
        parallel_tool(c,Y),
        b,
    )
    Z = intersection_tool(
        parallel_tool(b,Y),
        c,
    )
    return segment_tool(X,Y), segment_tool(Y,Z)
