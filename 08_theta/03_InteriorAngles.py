from constructions import *

def init(env):
    X = env.add_free(232.5, 268.5, hidden = True)
    Y = env.add_free(632.5, 210.5, hidden = True)
    Z = env.add_free(621.5, 396.5, hidden = True)
    A = env.add_free(351.5, 119.5)
    l1 = env.add_line(X, Y)
    l2 = env.add_line(X, Z)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, l1, l2)

def construct_goals(A, l1, l2):
    if np.dot(l1.n, l2.n) >= 0: n_base = l1.n + l2.n
    else: n_base = vector_perp_rot(l1.n - l2.n)
    return [
        (Line(n, np.dot(A.a, n)),)
        for n in (vector_perp_rot(n_base), n_base)
    ]

def additional_bb(A, l1, l2, goal):
    return (
        intersection_tool(l1, l2),
        intersection_tool(l1, goal),
        intersection_tool(l2, goal),
    )
