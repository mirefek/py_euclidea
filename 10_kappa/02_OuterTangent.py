from constructions import *

def rand_circle():
    return random_point(), np.random.lognormal(-1)

def init(env):
    c1 = env.add_free_circ(
        (417.5, 265.5), 123.15,
        hidden_center = False,
        rand_init = rand_circle,
    )
    c2 = env.add_free_circ(
        (207.0, 272.5), 46.0,
        hidden_center = False,
        rand_init = rand_circle,
    )

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(c1, c2)

def construct_goals(c1, c2):
    if c1.r > c2.r: c1, c2 = c2, c1
    C1 = Point(c1.c)
    C2 = Point(c2.c)
    c3 = Circle(c2.c, c2.r-c1.r)
    result = []
    for X in reversed(intersection_tool(c3, circle_by_diameter(C1,C2))):
        t = line_tool(C1, X)
        if np.dot(t.n, c2.c) > t.c: t.c -= c1.r
        else: t.c += c1.r
        result.append((t,))
    return result
