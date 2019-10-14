from constructions import *

def init(env):
    A = env.add_free(263.0, 116.0, hidden = True)
    B = env.add_free(488.5, 335.0, hidden = True)
    C = env.add_free(140.0, 335.0, hidden = True)
    X = env.add_free(280.0, 181.5, hidden = True)
    l1 = env.add_line(A,B)
    l2 = env.add_line(A,C)
    l3 = env.add_line(B,C)
    l4 = env.add_constr(parallel_tool, (l3,X), Line)
    M = env.add_free(296.5, 235.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(l1,l2,l3,l4,M)

def construct_goals(l1,l2,l3_in,l4_in,M):
    result = []
    for (l3,l4) in (l3_in,l4_in), (l4_in,l3_in):
        A = intersection_tool(l1, reflect_by_point(l3, M))
        B = intersection_tool(l2, reflect_by_point(l4, M))
        C = reflect_by_point(A, M)
        D = reflect_by_point(B, M)
        result.append((
            segment_tool(A,B),
            segment_tool(B,C),
            segment_tool(C,D),
            segment_tool(D,A),
        ))
    return result
