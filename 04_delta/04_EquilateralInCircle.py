from constructions import *
import itertools

def init(env):
    C = env.add_free(330.7, 253.0, hidden = True)
    A = env.add_free(443.5, 253.5)
    env.add_circle(C, A)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(C, A)

def construct_goals(C, A):
    C = C.a
    A = A.a
    vertices = [
        C + rotate_vector(A - C, ang)
        for ang in (0, -2*np.pi/3, 2*np.pi/3)
    ]
    return [
        Segment(X, Y)
        for (X, Y) in itertools.combinations(vertices, 2)
    ]

