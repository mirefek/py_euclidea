from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (143.0, 309.5), (392.5, 310.0))
    X,Y,_ = env.add_free_segment(
        (396.5, 114.5), (450.0, 155.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,X,Y)

def construct_goals(A,B,X,Y):
    circ = circle_by_diameter(A,B)
    leg_len = np.linalg.norm(Y.a-X.a)
    result = []
    for X in B.a, A.a:
        leg_circ = Circle(X, leg_len)
        for C in intersection_tool(circ, leg_circ):
            result.append((segment_tool(A, C), segment_tool(B, C)))
    return result

