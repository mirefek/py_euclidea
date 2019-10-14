from constructions import *

def init(env):
    A = env.add_free(334.0, 316.0, hidden = True)
    B = env.add_free(376.5, 199.5, hidden = True)
    C = env.add_free(442.0, 316.0, hidden = True)
    a = env.add_line(B,C)
    b = env.add_line(C,A)
    c = env.add_line(A,B)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C, a,b,c)

def construct_goals(A,B,C, a,b,c):
    la,lb,lc = (
        np.linalg.norm(Y.a-X.a)
        for (X,Y) in ((B,C), (C,A), (A,B))
    )
    result = []
    for i in range(3):
        X,Y,Z = rot_args(i, A.a,B.a,C.a)
        x,y,z = rot_args(i, a,b,c)
        lx,ly,lz = rot_args(i, la,lb,lc)
        center = (lx*X + ly*Y - lz*Z)/(lx+ly-lz)
        radius = z.dist_from(center)
        result.append((Circle(center, radius),))
    return result

def additional_bb(A,B,C, a,b,c, goal):
    return A,B,C
