from constructions import *

def init(env):
    A = env.add_free(303.5, 165.0)
    l1 = env.add_free_line(
        (13.5, 281.5), (627.5, 281.5))
    X = env.add_free(223.5, 343.5, hidden = True)
    l2 = env.add_constr(parallel_tool, (l1, X), Line)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, l1, l2)

def construct_goals(A, l1, l2):
    result = []
    for ang in np.pi/3, -np.pi/3:
        B = intersection_tool(
            l1,
            rotate_about_point(l2, A, -ang)
        )
        C = rotate_about_point(B, A, ang)
        result.append((
            segment_tool(A,B),
            segment_tool(B,C),
            segment_tool(C,A),
        ))
    return result
