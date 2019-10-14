from constructions import *

def rand_circ(l):
    radius = np.random.lognormal()
    center = random_point() + radius * 1.5 * l.n
    return center, radius

def init(env):
    l = env.add_free_line(
        (35.0, 365.0), (609.5, 365.0))
    circ = env.add_free_circ(
        (310.0, 199.0), 73.05,
        hidden_center = False,
        rand_init = (rand_circ, l),
    )

    env.set_tools(
        "move", "point", "line", "intersection",
    )
    env.goal_params(circ, l)

def construct_goals(circ, l):
    return Line(l.v, np.dot(l.v, circ.c))

def additional_bb(circ, l, goal):
    return Point(l.closest_on(circ.c))
