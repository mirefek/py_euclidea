from constructions import *
from itertools import combinations

def init(env):
    Fa = env.add_free(308.5, 162.0)
    Fb = env.add_free(272.5, 318.5)
    Fc = env.add_free(352.0, 329.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(Fa, Fb, Fc)

def construct_goals(Fa, Fb, Fc):
    a = ext_angle_bisector(Fb,Fa,Fc)
    b = ext_angle_bisector(Fc,Fb,Fa)
    c = ext_angle_bisector(Fa,Fc,Fb)
    vertices = (intersection_tool(x,y)
                for (x,y) in combinations((a,b,c),2))
    return [
        segment_tool(X,Y)
        for (X,Y) in combinations(vertices,2)
    ]
