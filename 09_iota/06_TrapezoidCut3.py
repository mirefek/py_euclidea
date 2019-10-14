from constructions import *

def init(env):
    (A,B,C,D),(a,b,c,d) = env.add_free_trapezoid(
        (478.0, 316.0), (167.5, 318.5), (304.0, 140.5), (434.5, 139.5))
    diag = env.add_segment(A,C)
    env.add_segment(B,D)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C,D, a,b,c,d, diag)

def construct_goals(A,B,C,D, a,b,c,d, diag):
    result = []
    for _ in range(2):
        X = intersection_tool(
            diag,
            line_tool(B, reflect_by_point(C, D))
        )
        line = parallel_tool(a, X)
        result.append((
            segment_tool(
                intersection_tool(line, b),
                intersection_tool(line, d),
            ),
        ))
        A,B,C,D = C,D,A,B
        a,b,c,d = c,d,a,b
    return result
