from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (268.0, 324.5), (397.5, 324.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(A, B)

def construct_goals(A_in, B_in):
    result = []
    for (A, B) in (A_in, B_in), (B_in, A_in):
        a60 = np.pi/3
        O = rotate_about_point(A, B, a60)
        vertices = [
            rotate_about_point(A, O, a60*i)
            for i in range(1,5)
        ]
        result.append(tuple(
            segment_tool(X,Y)
            for X,Y in zip([A]+vertices, vertices+[B])
        ))
    return result
