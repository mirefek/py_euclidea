from constructions import *

def init(env):
    X = env.add_free(311.5, 371.0)
    A = env.add_free(278.5, 223.0, hidden = True)
    B = env.add_free(355.0, 263.0, hidden = True)
    C = env.add_free(404.5, 230.5, hidden = True)
    la = env.add_line(A, B)
    lb = env.add_line(B, C)
    lc = env.add_constr(parallel_tool, (la, C), Line)
    ld = env.add_constr(parallel_tool, (lb, A), Line)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(A, B, C, la, lb, lc, ld, X)

def construct_goals(A, B, C, la, lb, lc, ld, X):
    result = []
    D = intersection_tool(lc, ld)
    for (p1, p2) in (B,D), (A,C):
        dir_line = line_tool(p1, p2)
        result.append((parallel_tool(dir_line, X),))
    return result

def additional_bb(A, B, C, la, lb, lc, ld, X, goal):
    return [
        intersection_tool(x,y)
        for (x,y) in ((la,lb), (lb,lc), (lc,ld), (ld,la),
                      (goal,la), (goal,lb), (goal,lc), (goal,ld))
    ]
