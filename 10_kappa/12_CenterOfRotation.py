from constructions import *

def init(env):
    A,B,_ = env.add_free_segment((304.5, 184.5), (410.5, 318.0))
    C = env.add_free(227.0, 322.0)
    circ = env.add_constr(
        compass_tool, (A,B,C), Circle, hidden = True)
    D = env.add_dep((355.5, 210.5), circ)
    env.add_segment(C,D)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B,C,D)

def construct_goals(A,B,C_in,D_in):
    return [
        (intersection_tool(
            perp_bisector_tool(A,C),
            perp_bisector_tool(B,D),
        ),)
        for (C,D) in ((C_in,D_in), (D_in,C_in))
    ]
