from constructions import *

def init(env):
    A = env.add_free(178.0, 357.5)
    B = env.add_free(466.0, 357.0)
    C = env.add_free(274.5, 136.5)
    env.add_segment(A, B)
    env.add_segment(B, C)
    env.add_segment(C, A)
    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "intersection",
    )
    env.goal_params(A, B, C)

def construct_goals(A, B, C):
    a,b,c = (
        np.linalg.norm(Y.a-X.a)
        for (X,Y) in ((B,C), (C,A), (A,B))
    )
    return Point((a*A.a + b*B.a + c*C.a)/(a+b+c))
