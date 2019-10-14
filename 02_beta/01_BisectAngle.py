from constructions import *

def init(env):
    A = env.add_free(175.5, 315.0)
    X = env.add_free(385.5, 19.0, hidden = True)
    Y = env.add_free(611.5, 320.0, hidden = True)
    env.add_ray(A, X)
    env.add_ray(A, Y)
    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "intersection",
    )
    env.goal_params(A, X, Y)

def construct_goals(A, X, Y):
    return angle_bisector_tool(X, A, Y)

def additional_bb(A, X, Y, goal):
    x = ray_tool(A,X).v
    y = ray_tool(A,Y).v
    return Point(A.a + x + y)
