from constructions import *

def init(env):
    O = env.add_free(319.5, 245)
    P = env.add_free(312.5, 125.5)
    env.add_circle(O, P)
    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "intersection",
    )
    env.goal_params(O, P)

def construct_goals(O, P):
    vertices = []
    v = P.a - O.a
    for _ in range(3):
        v = vector_perp_rot(v)
        vertices.append(Point(O.a + v))
    result = [
        segment_tool(X,Y)
        for X,Y in zip([P]+vertices, vertices+[P])
    ]
    return result
