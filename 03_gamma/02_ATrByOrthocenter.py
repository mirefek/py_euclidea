from constructions import *

def init(env):
    A, ray1, ray2 = env.add_free_angle(
        (158.0, 293.5), (578.0, 295.0), (542.5, 24.5))
    H = env.add_free(388.5, 207.0, rand_init = False)
    env.add_rand_init(H, random_point_in_angle, (ray1, ray2))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(A, ray1, ray2, H)

def construct_goals(A, ray1, ray2, H):
    alt1 = perp_tool(ray1, H)
    alt2 = perp_tool(ray2, H)
    B = intersection_tool(alt1, ray2)
    C = intersection_tool(alt2, ray1)
    return segment_tool(B, C)
