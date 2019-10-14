from constructions import *

def rand_circ(A, l):
    center = random_point()
    if (np.dot(A.a, l.n)-l.c) * (np.dot(center, l.n)-l.c) < 0:
        center = reflect_by_line(Point(center), l).a
    r = np.random.lognormal()
    if np.dot(A.a, l.n) > l.c: center += r*l.n
    else: center -= r*l.n
    center += r*l.v
    return center, r

def init(env):
    A = env.add_free(425.5, 248.5)
    l = env.add_free_line(
        (18.5, 344.5), (605.5, 352.5))
    circ = env.add_free_circ(
        (235.5, 175.0), 93.0,
        hidden_center = False,
        rand_init = (rand_circ, A, l),
    )

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(circ, A, l)

def construct_goals(circ, A, l):
    p = perp_tool(l, A)
    C = Point(circ.c)
    rad = radical_axis(
        circ,
        circle_tool(intersection_tool(p,l), A),
    )
    X = intersection_tool(p, rad)
    Bs = intersection_tool(circle_by_diameter(X, C), circ)
    result = []
    for B in Bs:
        C_res = intersection_tool(perp_bisector_tool(A, B), l)
        result.append((circle_tool(C_res, A), C_res))
    return result
