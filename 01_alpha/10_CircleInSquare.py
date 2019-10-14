from constructions import *

def init(env):
    (A,B,C,D),_ = env.add_free_square((218, 351), (419, 351.5))
    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "intersection",
    )
    env.goal_params(A, B, C, D)

def construct_goals(A, B, C, D):
    center = (A.a + C.a)/2
    radius = np.linalg.norm(B.a-A.a)/2
    return Circle(center, radius)
