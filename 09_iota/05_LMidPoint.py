from constructions import *

def init(env):
    A,B,seg = env.add_free_segment(
        (197.5, 258.5), (376.0, 123.0))
    X = env.add_free(366.5, 292.0, hidden = True)
    l = env.add_constr(parallel_tool, (seg, X), Line)

    env.set_tools(
        "move", "point", "line", "intersection",
    )
    env.goal_params(A, B, l)

def construct_goals(A, B, l):
    return midpoint_tool(A, B)

def additional_bb(A, B, l, goal):
    return reflect_by_line(goal, l)
