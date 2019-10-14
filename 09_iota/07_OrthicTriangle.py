from constructions import *
import itertools

def init(env):
    (A,B,C),_ = env.add_free_triangle(
        (340.5, 136.5), (189.0, 328.0), (471.0, 323.0),
        acute_prob = 1
    )

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    vertices = [
        line_tool(X, Y).closest_on(Z.a)
        for (X,Y,Z) in rots_args(A,B,C)
    ]
    return [
        Segment(X,Y)
        for (X,Y) in itertools.combinations(vertices, 2)
    ]
