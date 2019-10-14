from constructions import *

def init(env):
    (A,B,C),(a,b,c) = env.add_free_triangle(
        (200.0, 311.5), (489.5, 314.5), (372.5, 126.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C, a)

def construct_goals(A, B, C, side):
    a,b,c = (
        np.linalg.norm(Y.a-X.a)
        for (X,Y) in ((B,C), (C,A), (A,B))
    )
    center = (a*A.a + b*B.a + c*C.a)/(a+b+c)
    radius = side.dist_from(center)
    return Circle(center, radius)
