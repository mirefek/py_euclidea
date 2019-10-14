from constructions import *
import itertools

def init(env):
    C = env.add_free(337.0, 243.0)
    A = env.add_free(434.0, 264.0)
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
    lines = []
    for ang in (0, -2*np.pi/3, 2*np.pi/3):
        v = rotate_vector(A - C, ang)
        X = C + v
        lines.append(Line(v, np.dot(v, X)))
    vertices = [
        intersection_tool(l1, l2)
        for (l1, l2) in itertools.combinations(lines, 2)
    ]
    return [
        segment_tool(X, Y)
        for (X, Y) in itertools.combinations(vertices, 2)
    ]
