from constructions import *

def init(env):
    A,ray1,ray2 = env.add_free_angle(
        (230.0, 268.0), (621.5, 268.0), (602.5, 115.0))
    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "intersection",
    )
    env.goal_params(ray1, ray2)

def construct_goals(ray1, ray2):
    result = []
    for (rx, ry) in (ray1, ray2), (ray2, ray1):
        n = ry.n * np.dot(ry.n, rx.v)
        v = rx.v - 2*n
        result.append((Ray(rx.start_point, v),))
    return result

def additional_bb(ray1, ray2, goal):
    if np.linalg.matrix_rank((ray2.v+goal.v, ray1.v)) <= 1:
        ray = ray1
    else: ray = ray2
    return Point(ray.start_point + ray.v)
