from constructions import *
from itertools import combinations

def triangle_from_lines(*lines):
    assert(len(lines) == 3)
    vertices = (intersection_tool(x,y)
                for (x,y) in combinations(lines,2))
    return [
        segment_tool(X,Y)
        for (X,Y) in combinations(vertices,2)
    ]

def init(env):
    C = env.add_free(318.5, 264.5)
    X = env.add_free(257.5, 208.5)
    circ = env.add_circle(C, X)
    Y = env.add_dep((318.5, 347.5), circ)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(C,circ,X,Y)

def construct_goals(C,circ, X_in, Y_in):
    result = []
    for X,Y in (X_in, Y_in), (Y_in, X_in):
        Z = reflect_by_line(X, line_tool(C,Y))
        result.append(triangle_from_lines(
            polar_tool(X, circ),
            polar_tool(Y, circ),
            polar_tool(Z, circ),
        ))
    l = line_tool(X,Y)
    c_base = np.dot(l.n, circ.c)
    if c_base > l.c: l.c = c_base + circ.r
    else: l.c = c_base - circ.r
    result.append(triangle_from_lines(
        polar_tool(X, circ),
        polar_tool(Y, circ),
        l,
    ))
    return result

def ini_check(C, circ, X, Y, goal, scale):
    for A in (X,Y):
        if not any(seg.contains(A.a) for seg in goal):
            return False
    return True
