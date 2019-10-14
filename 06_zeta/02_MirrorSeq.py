from constructions import *

def init(env):
    A,B,_ = env.add_free_segment(
        (246.5, 171.0), (191.0, 301.0))
    l = env.add_free_line(
        (332.0, 7.0), (331.0, 478.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "intersection",
    )
    env.goal_params(A,B,l)

def construct_goals(A,B,l):
    A2 = reflect_by_line(A,l)
    B2 = reflect_by_line(B,l)
    return (
        A2, B2, segment_tool(A2,B2)
    )
