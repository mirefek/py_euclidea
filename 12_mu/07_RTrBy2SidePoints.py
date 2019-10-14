from constructions import *

def rand_init(circ):
    C = random_point_in_circle(circ)
    n = C - circ.c
    X,Y = intersection_tool(Line(n, np.dot(n, C)), circ)
    min_rad = circ.r - np.linalg.norm(C - circ.c)
    max_rad = np.linalg.norm(X.a - Y.a)/2
    r = np.random.uniform(min_rad, max_rad)
    X,Y = intersection_tool(Circle(C, r), circ)
    angles = [
        np.angle(complex(*(A.a - C)))
        for A in (X,Y)
    ]
    angles.sort()
    if angles[1] - angles[0] < np.pi:
        angles[0] += 2*np.pi
        angles.sort()
    ang = np.random.uniform(angles[0]+np.pi, angles[1])
    v = r*unit_vector(ang)
    return C+v, C-v

def init(env):
    circ = env.add_free_circ((324.5, 256.0), 136.25, hidden_center = False)
    Sa = env.add_free(255.0, 194.5, rand_init = False)
    Sb = env.add_free(383.0, 164.5, rand_init = False)
    env.add_rand_init((Sa, Sb), rand_init, (circ,))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(circ, Sa, Sb)

def construct_goals(circ, Sa, Sb):
    circ2 = circle_by_diameter(Sa, Sb)
    O = Point(circ.c)
    result = []
    for C in intersection_tool(circ, circ2):
        AB = []
        for S in Sa,Sb:
            p = perp_tool(line_tool(C, S), O)
            AB.append(reflect_by_line(C, p))
        A,B = AB
        result.append(
            (segment_tool(A,B), segment_tool(B,C), segment_tool(C,A)))
    return result

def ini_check(circ, Sa, Sb, goal, scale):
    return all(
        circ.dist_from(X.a) > 10/scale
        for X in (Sa, Sb)
    )
