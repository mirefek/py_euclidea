from constructions import *

def init(env):
    X = env.add_free(245.5, 300.0)
    Y = env.add_free(367.0, 210.5)
    Z = env.add_free(405.5, 284.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(X,Y,Z)

def construct_goals(X_in, Y_in, Z_in):
    result = []
    for (X,Y,Z) in (X_in,Y_in,Z_in), (Y_in,Z_in,X_in), (Z_in,X_in,Y_in):
        v = Z.a - (X.a+Y.a)/2
        A = Point(X.a+v)
        B = Point(Y.a+v)
        C = Point(Y.a-v)
        D = Point(X.a-v)
        result.append((
            segment_tool(A,B),
            segment_tool(B,C),
            segment_tool(C,D),
            segment_tool(D,A),
        ))
    return result
