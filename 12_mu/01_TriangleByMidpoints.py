from constructions import *
from itertools import combinations

def init(env):
    A = env.add_free(315.5, 183.5)
    B = env.add_free(453.0, 261.5)
    C = env.add_free(283.5, 304.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C)

def construct_goals(A, B, C):
    a = parallel_tool(line_tool(B, C), A)
    b = parallel_tool(line_tool(C, A), B)
    c = parallel_tool(line_tool(A, B), C)
    vertices = (intersection_tool(x,y)
                for (x,y) in combinations((a,b,c),2))
    return [
        segment_tool(X,Y)
        for (X,Y) in combinations(vertices,2)
    ]
