from constructions import *

def init(env):
    (A,B,C),_ = env.add_free_triangle(
        (428.5, 138.5), (173.0, 334.0), (444.5, 327.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    result = []
    for (X,Y,Z) in (A,B,C),(B,C,A),(C,A,B):
        x,y,z = (
            np.linalg.norm(p2.a-p1.a)
            for (p1,p2) in ((Y,Z), (Z,X), (X,Y))
        )
        P = Point((0.5 + (z-y)/(2*x))*Y.a + (0.5 + (y-z)/(2*x))*Z.a)
        result.append((segment_tool(X,P),))
    return result
