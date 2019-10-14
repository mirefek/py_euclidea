from constructions import *

def init(env):
    A = env.add_free(224.5, 337.5)
    X1 = env.add_free(419.5, 337.0)
    ray = env.add_ray(A, X1)
    Y1 = env.add_dep((350.5, 337.5), ray)
    X2, X3 = env.add_constr(square_vertices, (A, X1), (Point, Point))
    Y2, Y3 = env.add_constr(square_vertices, (A, Y1), (Point, Point))
    env.add_ray(A,X3)
    for p1,p2 in (X1,X2),(X2,X3),(Y1,Y2),(Y2,Y3):
        env.add_segment(p1,p2)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, X1, Y1, ray)

def construct_goals(A, X1, Y1, ray):
    x = np.linalg.norm(X1.a - A.a)
    y = np.linalg.norm(Y1.a - A.a)
    z = np.sqrt(x**2 + y**2)
    Z1 = Point(A.a + z * ray.v)
    Z2, Z3 = square_vertices(A, Z1)
    return segment_tool(Z1,Z2), segment_tool(Z2,Z3)
