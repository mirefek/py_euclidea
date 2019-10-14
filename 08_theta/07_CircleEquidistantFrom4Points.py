from constructions import *

def init(env):
    A = env.add_free(204.0, 348.0)
    B = env.add_free(229.5, 194.5)
    C = env.add_free(328.5, 252.0)
    D = env.add_free(421.5, 271.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C,D)

def construct_goals(A,B,C,D):
    result = []
    for (U,V,X,Y) in (A,B,C,D),(A,C,B,D),(A,D,B,C):
        center = intersection_tool(
            perp_bisector_tool(U,V),
            perp_bisector_tool(X,Y),
        ).a
        radius = (U.dist_from(center) + X.dist_from(center))/2
        result.append((Circle(center, radius),))
    return result

def ini_check(A,B,C,D,goal,scale):
    return goal.dist_from(A.a) > 10 / scale
