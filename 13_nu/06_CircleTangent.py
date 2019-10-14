from constructions import *

def init(env):
    A = env.add_free(255.5, 248.5)
    B = env.add_free(314.0, 160.0)
    l = env.add_free_line(
        (56.0, 329.5), (618.0, 328.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, l)

def construct_goals(A, B, l):
    center = intersection_tool(line_tool(A, B), l).a
    radius = np.sqrt(A.dist_from(center) * B.dist_from(center))
    bis = perp_bisector_tool(A,B)
    result = []
    for T in intersection_tool(Circle(center, radius), l):
        C = intersection_tool(perp_tool(l, T), bis)
        result.append((circle_tool(C,T),))
    return result

def ini_check(A, B, l, goal, scale):
    return goal.contains(A.a) and goal.contains(B.a)
    
