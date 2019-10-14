from constructions import *

def init(env):
    A = env.add_free(303.5, 165.0)
    l1 = env.add_free_line(
        (21.5, 241.0), (621.0, 243.0))
    X = env.add_free(262.5, 333.0, hidden = True)
    l2 = env.add_constr(parallel_tool, (l1, X), Line)

    env.set_tools(
        "move", "point", "line", "intersection",
    )
    env.goal_params(A, l1, l2)

def construct_goals(A, l1, l2):
    return parallel_tool(l1, A)

def additional_bb(A, l1, l2, goal):
    res = []
    for l in (l1, l2):
        X = l.closest_on(A.a)
        res += [Point(a*A.a + (1-a)*X) for a in (-0.5, 1.5)]
    return res
