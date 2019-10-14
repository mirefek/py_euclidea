from constructions import *

def init(env):
    A = env.add_free(143.0, 384.0)
    B = env.add_free(483.0, 147.5)
    C = env.add_free(218.5, 220.0)
    D = env.add_free(455.0, 351.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C, D)

def construct_goals(A, B, C, D):
    v_base = vector_perp_rot(D.a - C.a)
    result = []
    for v in v_base, -v_base:
        X = Point(A.a + v)
        l1 = line_tool(X, B)
        l2 = parallel_tool(l1, A)
        l3 = perp_tool(l1, C)
        l4 = perp_tool(l1, D)
        result.append((l1,l2,l3,l4))
    return result

def additional_bb(A,B,C,D,goal):
    l1,l2,l3,l4 = goal
    return (
        intersection_tool(l1,l3),
        intersection_tool(l1,l4),
        intersection_tool(l2,l3),
        intersection_tool(l2,l4),
    )
