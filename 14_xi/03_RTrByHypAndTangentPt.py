from constructions import *

def init(env):
    A,B,seg = env.add_free_segment(
        (180.5, 284.0), (467.0, 285.0))
    T = env.add_dep((268.5, 284.5), seg)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, seg, T)

def construct_goals(A, B, seg, T):
    result = []
    O = midpoint_tool(A, B)
    Ms = intersection_tool(
        perp_bisector_tool(A,B), circle_by_diameter(A,B)
    )
    for M in Ms:
        
        I = min(
            intersection_tool(circle_tool(M,A), perp_tool(seg,T)),
            key = lambda X: seg.dist_from(X.a)
        )
        C = reflect_by_line(M, perp_tool(line_tool(M, I), O))
        result.append((segment_tool(C,A), segment_tool(C,B)))

    return result
