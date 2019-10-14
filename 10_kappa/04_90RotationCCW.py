from constructions import *

def init(env):
    A,B,_ = env.add_free_segment((169.0, 250.0), (270.5, 136.0))
    C = env.add_free(364.0, 207.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C)

def construct_goals(A, B, C):
    A2 = rotate_about_point(A, C, -np.pi/2)
    B2 = rotate_about_point(B, C, -np.pi/2)
    return A2, B2, segment_tool(A2, B2)
