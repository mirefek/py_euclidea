from constructions import *

def init(env):
    B, a, c = env.add_free_angle(
        (156.0, 286.5), (546.0, 26.5), (611.5, 286.0))
    M = env.add_free(369.5, 184.0, rand_init = False)
    env.add_rand_init(M, random_point_in_angle, (a, c))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(B, a, c, M)

def construct_goals(B, a, c, M):
    D = intersection_tool(perp_bisector_tool(B, M), a)
    E1, E2 = intersection_tool(circle_tool(M, D), c)
    l2 = segment_tool(D, M)
    return [
        (l2, segment_tool(M, E))
        for E in (E1, E2)
        if E is not None
    ]
