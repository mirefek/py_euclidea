from constructions import *

def rand_circle():
    return random_point(), np.random.lognormal(-1)

def init(env):
    circ1 = env.add_free_circ(
        (429.5, 161.0),
        85.95,
        hidden_center = False,
        rand_init = rand_circle,
    )
    circ2 = env.add_free_circ(
        (231.0, 286.0), 113.1,
        hidden_center = False,
        rand_init = rand_circle,
    )
    T = env.add_dep((343.5, 298.0), circ2)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(circ1, circ2, T)

def construct_goals(circ1, circ2, T):
    l = line_tool(Point(circ2.c), T)
    C1 = Point(circ1.c)
    result = []
    for v in -l.v, l.v:
        C = intersection_tool(
            l,
            perp_bisector_tool(
                C1, Point(T.a + circ1.r * v)
            )
        )
        result.append((circle_tool(C,T),))

    return result
