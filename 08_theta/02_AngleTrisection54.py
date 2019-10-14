from constructions import *

def rotate_ray54(ray):
    return rotate_ray(ray, -3*np.pi/10)

def init(env):
    A,_,ray1 = env.add_free_ray((178.0, 325.5), (614.0, 325.5))
    ray2 = env.add_constr(rotate_ray54, (ray1,), Ray)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(ray1)

def construct_goals(ray1):
    return rotate_ray(ray1, -np.pi/10), rotate_ray(ray1, -np.pi/5)

def additional_bb(ray, goal):
    return Point(ray.start_point + goal[0].v + goal[1].v)
