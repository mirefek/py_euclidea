from constructions import *

def init(env):
    A = env.add_free(283.5, 194.5, rand_init = False)
    B = env.add_free(377.5, 201.5, rand_init = False)
    C = env.add_free(328.0, 290.0, rand_init = False)
    env.add_rand_init((A,B,C), random_triangle,
                      kwargs = {"acute_prob" : 0.7})

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    circ = circumcircle_tool(A,B,C)
    a,b,c = (
        polar_tool(X, circ) for X in (A,B,C)
    )
    return (
        circle_tool(intersection_tool(b,c), B),
        circle_tool(intersection_tool(c,a), C),
        circle_tool(intersection_tool(a,b), A),
    )
