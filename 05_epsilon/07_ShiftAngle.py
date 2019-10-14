from constructions import *

def init(env):
    A, rx, ry = env.add_free_angle(
        (156.0, 316.5), (631.5, 328.5), (437.0, 14.0))
    X = env.add_free(310.0, 226.0, rand_init = False)
    env.add_rand_init(X, random_point_in_angle, (ry, rx))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(X, rx, ry)

def construct_goals(X, rx, ry):
    return (Ray(X.a, rx.v), Ray(X.a, ry.v))

def additional_bb(X, rx, ry, goal):
    return Point(2*X.a - rx.start_point)
