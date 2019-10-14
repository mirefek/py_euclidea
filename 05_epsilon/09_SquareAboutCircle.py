from constructions import *

def line_init():
    X = random_point()
    Y = random_point()
    v = vector_perp_rot(X-Y)
    return X+v, Y+v

def init(env):
    circ = env.add_free_circ((309.5, 199.0), 73.0, hidden_center = False)
    X = env.add_free((17.0, 365.0), hidden = True, rand_init = False)
    Y = env.add_free((623.5, 365.0), hidden = True, rand_init = False)
    env.add_rand_init((X, Y), line_init)
    dir_line = env.add_line(X, Y)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(circ, dir_line)

def construct_goals(circ, dir_line):
    O = circ.c
    v1 = circ.r * dir_line.n
    v2 = circ.r * dir_line.v
    A = O+v1+v2
    B = O+v1-v2
    C = O-v1-v2
    D = O-v1+v2
    return (
        Segment(A, B),
        Segment(B, C),
        Segment(C, D),
        Segment(D, A),
    )

def additional_bb(circ, dir_line, goal):
    return Point(dir_line.closest_on(circ.c))
