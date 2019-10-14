from constructions import *

def init(env):
    A,B,_ = env.add_free_segment((247.4, 242.5), (405.5, 241))
    env.set_tools("perp_bisector")
    env.goal_params(A, B)

def construct_goals(A, B):
    return (
        perp_bisector_tool(A, B),
    )
