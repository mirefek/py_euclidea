from constructions import *

def init(env):
    Ea = env.add_free(176.0, 167.5, rand_init = False)
    Eb = env.add_free(492.5, 175.5, rand_init = False)
    Ec = env.add_free(344.5, 392.5, rand_init = False)
    env.add_rand_init((Ea,Eb,Ec), random_triangle, kwargs = {"acute_prob": 1})

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(Ea, Eb, Ec)

def construct_goals(Ea, Eb, Ec):
    A = Point(line_tool(Eb,Ec).closest_on(Ea.a))
    B = Point(line_tool(Ec,Ea).closest_on(Eb.a))
    C = Point(line_tool(Ea,Eb).closest_on(Ec.a))
    return segment_tool(A,B), segment_tool(B,C), segment_tool(C,A)
