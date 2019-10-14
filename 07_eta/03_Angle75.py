from constructions import *

def init(env):
    _,_,ray = env.add_free_ray((258.0, 268.0), (384, 268))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(ray)

def construct_goals(ray):
    angle = 5*np.pi / 12
    vecs = (rotate_vector(ray.v, ang) for ang in (-angle, angle))
    X = ray.start_point
    return tuple(
        (Ray(X, v),)
        for v in vecs
    )

def additional_bb(ray, goal):
    return Point(ray.start_point + ray.v + goal.v)
