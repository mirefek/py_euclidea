from constructions import *

def init(env):
    _,_,ray = env.add_free_ray(
        (230.0, 268.0), (623.0, 268.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(ray)

def construct_goals(ray):
    vecs = (rotate_vector(ray.v, ang) for ang in (-np.pi/4, np.pi/4))
    X = ray.start_point
    return tuple(
        (Ray(X, v),)
        for v in vecs
    )

def additional_bb(ray, goal):
    return Point(ray.start_point + ray.v + goal.v)
