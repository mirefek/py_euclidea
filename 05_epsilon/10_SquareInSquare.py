from constructions import *

def init(env):
    (A,B,C,D),(a,b,c,d) = env.add_free_square(
        (420.0, 151.0), (219.0, 150.0))
    X = env.add_dep((274.0, 150.5), a)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(A,B,C,D,X)

def construct_goals(A,B,C,D,X):
    O = (A.a+B.a+C.a+D.a)/4
    v = X.a - O
    vertices = []
    for _ in range(3):
        v = vector_perp_rot(v)
        vertices.append(Point(O + v))
    return [
        segment_tool(p1,p2)
        for p1,p2 in zip([X]+vertices, vertices+[X])
    ]

