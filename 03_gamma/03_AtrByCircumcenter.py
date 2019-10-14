from constructions import *

def init(env):
    A, ray1, ray2 = env.add_free_angle(
        (224.5, 298.0), (580.5, 301.0), (508.5, 31.5))
    O = env.add_free(378.0, 258.0, rand_init = False)
    env.add_rand_init(O, random_point_in_angle, (ray1, ray2))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(A, ray1, ray2, O)

def construct_goals(A, ray1, ray2, O):
    endpoints = [
        A.a + 2 * ray.v * np.dot(ray.v, O.a-A.a)
        for ray in (ray1, ray2)
    ]
    return Segment(*endpoints)
