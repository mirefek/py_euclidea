from constructions import *

def init(env):
    A, B, _ = env.add_free_segment((274.5, 225.5), (391.5, 226))
    env.set_tools("move", "point", "line", "circle", "intersection")
    env.goal_params(A, B)

def construct_goals(A, B):
    C0, C1 = intersection_tool(
        circle_tool(A, B),
        circle_tool(B, A),
    )
    return (
        (segment_tool(C0, A), segment_tool(C0, B)),
        (segment_tool(C1, A), segment_tool(C1, B)),
    )
