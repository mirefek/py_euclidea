from constructions import *

def init(env):
    A = env.add_free(227.0, 264.5)
    B = env.add_free(406.0, 263.5)
    seg = env.add_segment(A,B, hidden = True)
    X = env.add_dep((289.5, 264.0), seg, hidden = True)
    Xa = env.add_constr(reflect_by_point, (X,A), Point, hidden = True)
    Xb = env.add_constr(reflect_by_point, (X,B), Point, hidden = True)
    M = env.add_constr(midpoint_tool, (Xa, Xb), Point)
    ca = env.add_circle(A, X)
    cb = env.add_circle(B, X)
    cm = env.add_circle(M, Xa)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(X, Xa, Xb)

def construct_goals(X, Xa, Xb):
    va = X.a - Xa.a
    vb = X.a - Xb.a
    n_base = vector_perp_rot(va-vb)/2
    r_sq = np.linalg.norm(va) * np.linalg.norm(vb)
    result = []
    for n in n_base, -n_base:
        A = va + 2*n
        B = vb + 2*n
        C = (va + vb)/2 + n
        # inverse
        A *= r_sq / np.linalg.norm(A)**2
        B *= r_sq / np.linalg.norm(B)**2
        C *= r_sq / np.linalg.norm(C)**2
        # finalize
        A = Point(X.a + A)
        B = Point(X.a + B)
        C = Point(X.a + C)
        result.append((circumcircle_tool(A, B, C),))
    return result
