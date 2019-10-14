from constructions import *

def init(env):
    A = env.add_free(225.5, 264.5)
    B = env.add_free(328.5, 186)
    C = env.add_free(443, 310)
    env.set_tools("line")
    env.goal_params(A, B, C)

def construct_goals(A, B, C):
    return (
        segment_tool(A, B),
        segment_tool(B, C),
        segment_tool(C, A),
    )
