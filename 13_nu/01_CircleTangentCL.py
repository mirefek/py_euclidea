from constructions import *

def rand_circ(l):
    r = np.random.lognormal(-1)
    center = random_point()
    if np.dot(l.n, center) - l.c > 0: center += l.n*r
    else: center -= l.n*r
    return center, r

def init(env):
    A = env.add_free(396.5, 365.0)
    X = env.add_free(7.0, 365.0, hidden = True)
    l = env.add_line(X, A)
    circ = env.add_free_circ(
        (246.0, 213.0), 79.6,
        hidden_center = False,
        rand_init = (rand_circ, l),
    )

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(circ, A, l)

def construct_goals(circ, A, l):
    X = intersection_tool(radical_axis(circ, A), l)
    return [
        (circle_tool(intersection_tool(
            perp_bisector_tool(A, T),
            perp_tool(l, A),
        ), A),)
        for T in intersection_tool(circ, circle_tool(X, A))
    ]

