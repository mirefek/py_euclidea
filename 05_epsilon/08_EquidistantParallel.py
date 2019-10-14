from constructions import *

def init(env):
    l1 = env.add_free_line((13.5, 204.0), (622.5, 204.0))
    X = env.add_free(342.0, 328.5, hidden = True)
    l2 = env.add_constr(parallel_tool, (l1, X), Line)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(l1, l2)

def construct_goals(l1, l2):
    if np.dot(l1.n, l2.n) > 0: c2 = l2.c
    else: c2 = -l2.c
    return Line(l1.n, (l1.c+c2)/2)

def additional_bb(l1, l2, goal):
    origin = np.array((0,0))
    return Point(l1.closest_on(origin)), Point(l2.closest_on(origin))
