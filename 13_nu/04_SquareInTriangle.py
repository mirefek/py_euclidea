from constructions import *

def init(env):
    (A,B,C),(a,b,c) = env.add_free_triangle(
        (156.5, 334.0), (326.5, 149.0), (479.5, 333.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, C, a, b, c)

def construct_goals(A, B, C, a, b, c):
    vb = B.a-A.a
    vc = C.a-A.a
    vc /= np.linalg.norm(vc)
    vb /= np.abs(np.dot(vb, vector_perp_rot(vc)))
    n = vector_perp_rot(vb+vc)
    V = intersection_tool(Line(n, np.dot(n, A.a)), a)
    U = intersection_tool(parallel_tool(b, V), c)
    X = intersection_tool(perp_tool(b, U), b)
    Y = intersection_tool(perp_tool(b, V), b)
    return (
        segment_tool(X,U),
        segment_tool(U,V),
        segment_tool(V,Y),
    )
