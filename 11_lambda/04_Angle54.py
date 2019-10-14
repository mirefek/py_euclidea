from constructions import *

def init(env):
    _,_,ray = env.add_free_ray(
        (178.5, 325.5), (622.5, 325.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(ray)

def construct_goals(ray):
    ang = 3*np.pi/10
    return (
        (rotate_ray(ray, -ang),),
        (rotate_ray(ray, ang),),
    )

def additional_bb(ray, goal):
    return Point(ray.start_point + ray.v + goal.v)
