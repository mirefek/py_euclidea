from constructions import *

def init(env):
    C = env.add_free(329.0, 247.0)
    A = env.add_free(329.5, 143.5)
    env.add_circle(C,A)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(C,A)

def construct_goals(C,A):
    ang = 2*np.pi/5
    vertices = [
        rotate_about_point(A,C,ang*i)
        for i in range(1,5)
    ]
    return [
        segment_tool(X,Y)
        for (X,Y) in zip([A]+vertices, vertices+[A])
    ]
