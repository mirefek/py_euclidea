from constructions import *
from itertools import combinations

def init(env):
    A = env.add_free(208.5, 240.5, rand_init = False)
    B = env.add_free(401.0, 241.5, rand_init = False)
    C = env.add_free(331.5, 397.5, rand_init = False)
    env.add_rand_init((A,B,C), random_triangle, kwargs = {"acute_prob": 1})

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C)

def construct_goals(A, B, C):
    circ = circumcircle_tool(A, B, C)
    a = polar_tool(A, circ)
    b = polar_tool(B, circ)
    c = polar_tool(C, circ)
    vertices = (intersection_tool(x,y)
                for (x,y) in combinations((a,b,c),2))
    return [
        segment_tool(X,Y)
        for (X,Y) in combinations(vertices,2)
    ]
