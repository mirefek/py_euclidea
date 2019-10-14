from constructions import *

def rand_init(l):
    C1 = random_point()
    C2 = random_point()+l.v
    if np.dot(l.n, C1) < l.c: C1 = reflect_by_line(Point(C1), l).a
    if np.dot(l.n, C2) < l.c: C2 = reflect_by_line(Point(C2), l).a

    dist = np.linalg.norm(C1 - C2)
    radii = dist * np.random.random(size = 2)
    radii.sort()
    r1, r2 = radii
    r2 -= r1
    if np.dot(C1, l.n)-r1 < np.dot(C2, l.n)-r2: shift = r1
    else: shift = r2
    shift = shift * l.n
    C1 += shift
    C2 += shift

    v = np.array((-0.4, 1.1))
    v /= np.linalg.norm(v)
    return C1, C1+r1*v, C2, C2+r2*v

def init(env):
    l = env.add_free_line(
        (37.0, 325.0), (612.0, 325.0))

    C1 = env.add_free(235.0, 198.0, rand_init = False)
    X1 = env.add_free(213.0, 258.5, rand_init = False, hidden = True)
    C2 = env.add_free(445.5, 205.0, rand_init = False)
    X2 = env.add_free(428.5, 251.7, rand_init = False, hidden = True)
    circ1 = env.add_circle(C1,X1)
    circ2 = env.add_circle(C2,X2)
    env.add_rand_init((C1,X1,C2,X2), rand_init, (l,))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(circ1, circ2, l)

def construct_goals(circ1, circ2, l):
    if circ1.r < circ2.r: circ1,circ2 = circ2,circ1
    C1 = Point(circ1.c)
    C2 = Point(circ2.c)
    p = perp_tool(l, C2)
    circ1_mod = Circle(circ1.c, abs(circ1.r-circ2.r))
    rad = radical_axis(
        circ1_mod,
        circle_tool(intersection_tool(p,l), C2),
    )
    X = intersection_tool(p, rad)
    Bs = intersection_tool(circle_by_diameter(X, C1), circ1_mod)

    result = []
    for B in Bs:
        C_res = intersection_tool(perp_bisector_tool(B, C2), l)
        r_res = C_res.dist_from(circ2.c)
        if r_res > C_res.dist_from(circ1.c): r_res += circ2.r
        else: r_res -= circ2.r
        result.append((Circle(C_res.a, r_res), C_res))
        #result.append((circle_tool(C_res, A), C_res))
    return result

