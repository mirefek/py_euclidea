from constructions import *

def init(env):
    A, ray1, ray2 = env.add_free_angle(
        (174.0, 286.0), (542.0, 7.0), (624.5, 342.5))
    M = env.add_free(348.5, 229.5, rand_init = False)
    env.add_rand_init(M, random_point_in_angle, (ray1, ray2))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, ray1, ray2, M)

def construct_goals(A, ray1, ray2, M):
    C = Point(2*M.a-A.a)
    B = intersection_tool(ray1, parallel_tool(ray2, C))
    D = intersection_tool(ray2, parallel_tool(ray1, C))
    return segment_tool(B,D)
