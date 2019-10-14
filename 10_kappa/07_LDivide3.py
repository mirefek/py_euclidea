from constructions import *

def init(env):
    A,B,seg = env.add_free_segment((197.5, 258.5), (333.5, 153.5))
    X = env.add_free(351.0, 303.0, hidden = True)
    l = env.add_constr(parallel_tool, (seg, X), Line)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B, l)

def construct_goals(A, B, l):
    return Point((2*A.a+B.a)/3), Point((A.a+2*B.a)/3)

def additional_bb(A, B, l, goal):
    return reflect_by_line(goal[0], l)
