from constructions import *

def init(env):
    C = env.add_free(268.0, 264.5)
    X = env.add_free(220.5, 341.5, hidden = True)
    Y = env.add_free(178.5, 388.5, hidden = True)
    A = env.add_free(498.0, 191.0)
    circ1 = env.add_circle(C,X)
    circ2 = env.add_circle(C,Y)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, circ1, circ2)

def construct_goals(A, circ1, circ2):
    result = []
    for ang in -np.pi/3, np.pi/3:
        Bs = intersection_tool(
            circ1,
            rotate_about_point(circ2, A, -ang)
        )
        for B in reversed(Bs):
            C = rotate_about_point(B, A, ang)
            result.append((
                segment_tool(A,B),
                segment_tool(B,C),
                segment_tool(C,A),
            ))
    return result

