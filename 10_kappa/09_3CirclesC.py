from constructions import *

def init(env):
    A = env.add_free(232.0, 311.5)
    B = env.add_free(340.5, 158.5)
    C = env.add_free(406.5, 314.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C)

def construct_goals(A, B, C):
    a,b,c = (
        np.linalg.norm(Y.a-X.a)
        for (X,Y) in ((B,C), (C,A), (A,B))
    )
    return (
        Circle(A.a, (b+c-a)/2),
        Circle(B.a, (c+a-b)/2),
        Circle(C.a, (a+b-c)/2),
    )
