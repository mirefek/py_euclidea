from constructions import *

def init(env):
    A = env.add_free(263, 285)
    B = env.add_free(398.5, 220.5)
    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "intersection",
    )
    env.goal_params(A, B)

def construct_goals(A, B):
    return (
        Point((A.a + B.a)/2)
    )
