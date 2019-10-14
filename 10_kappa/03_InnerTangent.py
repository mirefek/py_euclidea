from constructions import *

def rand_circle():
    return random_point(), np.random.lognormal(-1)

def init(env):
    c1 = env.add_free_circ(
        (450.0, 268.0), 93.7,
        hidden_center = False,
        rand_init = rand_circle,
    )
    c2 = env.add_free_circ(
        (171.0, 272.5), 58.7,
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
    C1 = Point(c1.c)
    C2 = Point(c2.c)
    c3 = Circle(c2.c, abs(c1.r+c2.r))
    result = []
    for X in intersection_tool(c3, circle_by_diameter(C1,C2)):
        t = line_tool(C1, X)
        if np.dot(t.n, c2.c) > t.c: t.c += c1.r
        else: t.c -= c1.r
        result.append((t,))
    return result

