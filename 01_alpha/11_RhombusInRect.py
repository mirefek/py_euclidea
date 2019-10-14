from constructions import *

def init(env):
    (A,B,C,D), _ = env.add_free_rectangle(
        (448, 312.5), (204.5, 312.5), (204.5, 142))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "intersection",
    )
    env.goal_params(A, B, C, D)

def construct_goals(A_in, B_in, C_in, D_in):
    M = (A_in.a+C_in.a)/2
    result = []
    for (A,B,C,D) in ((A_in, B_in, C_in, D_in),
                      (D_in, C_in, B_in, A_in)):
        diag = perp_bisector_tool(B, D)
        ab = line_tool(A,B)
        cd = line_tool(C,D)
        X_ab = Point(intersection_ll(ab, diag))
        X_cd = Point(intersection_ll(cd, diag))
        result.append((segment_tool(B, X_cd),
                       segment_tool(D, X_ab)))
    return result

def ini_check(A, B, C, D, goal, scale):
    return B.dist_from(A.a) > B.dist_from(C.a)
