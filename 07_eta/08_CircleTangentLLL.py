from constructions import *

def init(env):
    A = env.add_free(136.0, 244.5, hidden = True)
    B = env.add_free(346.5, 379.5, hidden = True)
    X = env.add_free(519.0, 4.5, hidden = True)
    l = env.add_line(A,B)
    p1 = env.add_line(A,X)
    p2 = env.add_constr(parallel_tool, (p1, B), Line)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,l,p1)

def construct_goals(A,B,l,p1):
    if np.dot(l.n, p1.n) > 0:
        n1 = vector_perp_rot(l.n+p1.n)
    else:
        n1 = l.n-p1.n
    n2 = vector_perp_rot(n1)
    result = []
    for (na, nb) in (n2, n1), (n1, n2):
        la = Line(na, np.dot(A.a, na))
        lb = Line(nb, np.dot(B.a, nb))
        center = intersection_tool(la, lb).a
        radius = l.dist_from(center)
        result.append((Circle(center, radius),))
    return result

def additional_bb(A,B,l,p1,goal):
    return A,B
