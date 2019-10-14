from constructions import *

def init(env):
    c0 = env.add_free_circ((232.5, 256), 119)
    c1 = env.add_free_circ((436, 267), 86)
    env.add_free_line((347, 0), (354.5, 490.5))
    env.set_tools("intersection")
    env.goal_params(c0, c1)

def construct_goals(c0, c1):
    return (
        intersection_tool(c0, c1),
    )
