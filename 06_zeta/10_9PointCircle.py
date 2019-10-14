from constructions import *

def init(env):
    (A,B,C),_ = env.add_free_triangle(
        (155.5, 360.5), (504.5, 360.5), (395.5, 149.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C)

def construct_goals(A,B,C):
    Ma = midpoint_tool(B,C)
    Mb = midpoint_tool(C,A)
    Mc = midpoint_tool(A,B)
    return circumcircle_tool(Ma,Mb,Mc)
