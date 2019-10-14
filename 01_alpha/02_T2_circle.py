from constructions import *

def init(env):
    O = env.add_free(303.5, 237.5)
    P = env.add_free(385.5, 186)
    env.set_tools("circle")
    env.goal_params(O, P)

def construct_goals(O, P):
    return circle_tool(O, P)
