from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (259.0, 236.5), (397.0, 236.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, B)

def construct_goals(A, B):
    phi = (np.sqrt(5)-1)/2
    return (
        (Point((1-phi)*A.a + phi*B.a),),
        (Point(phi*A.a + (1-phi)*B.a),),
    )
