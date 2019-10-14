from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (184.5, 311.5), (281.5, 259.5))
    l = env.add_line(A,B, hidden = True)
    C = env.add_dep((419.5, 185.5), l)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    v_base = B.a-A.a
    result = []
    for v in v_base, -v_base:
        result.append((Point(C.a+v),))
    return result
