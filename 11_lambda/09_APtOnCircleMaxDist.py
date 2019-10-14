from constructions import *

def circle_in_angle(ray1, ray2):
    radius = np.random.lognormal()
    A = ray1.start_point
    v = ray1.v + ray2.v
    d = ray1.dist_from(A+v)
    A2 = A + v * (1.1*radius/d)
    center = random_point_in_angle(Ray(A2, ray1.v), Ray(A2, ray2.v))
    print(center, radius)
    return center, radius

def init(env):
    A,ray1,ray2 = env.add_free_angle(
        (108.0, 373.5), (535.0, 14.0), (628.0, 373.0))
    circ = env.add_free_circ(
        (373.0, 245.5), 60.4,
        hidden_center = False,
        rand_init = (circle_in_angle, ray1, ray2),
    )

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(ray1, ray2, circ)

def construct_goals(ray1, ray2, circ):
    if np.dot(ray1.n, ray2.n) >= 0: n = ray1.n + ray2.n
    else: n = vector_perp_rot(ray1.n - ray2.n)
    return max(
        intersection_tool(circ, Line(n, np.dot(circ.c, n))),
        key = lambda X: ray1.dist_from(X.a) + ray2.dist_from(X.a)
    )

def additional_bb(ray1, ray2, circ, goal):
    return (
        Point(ray1.closest_on(goal.a)),
        Point(ray2.closest_on(goal.a)),
    )
