from constructions import *

def init(env):
    circ = env.add_free_circ((329.0, 247.0), 118.65, hidden_center = False)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(circ)

def construct_goals(circ):
    return Circle(circ.c, circ.r/np.sqrt(2))
