from constructions import *

def init(env):
    (A,B,C),_ = env.add_free_triangle(
        (296.5, 137.0), (188.0, 329.0), (472.5, 322.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C)

def construct_goals(A, B, C):
    result = []
    for ang in -np.pi/3, np.pi/3:
        C2 = rotate_about_point(A, B, ang)
        A2 = rotate_about_point(B, C, ang)
        result.append((intersection_tool(
            line_tool(A, A2),
            line_tool(C, C2),
        ),))
    return result
