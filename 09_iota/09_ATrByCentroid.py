from constructions import *

def init(env):
    A,ray1,ray2 = env.add_free_angle(
        (156.0, 303.5), (507.0, 16.5), (614.0, 293.5))
    G = env.add_free(327.0, 220.0, rand_init = False)
    env.add_rand_init(G, random_point_in_angle, (ray1, ray2))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, ray1, ray2, G)

def construct_goals(A, ray1, ray2, G):
    C = Point(3*G.a-2*A.a)
    B = intersection_tool(ray1, parallel_tool(ray2, C))
    D = intersection_tool(ray2, parallel_tool(ray1, C))
    return segment_tool(B,D)
