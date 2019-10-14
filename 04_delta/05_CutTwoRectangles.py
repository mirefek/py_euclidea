from constructions import *

def init(env):
    vert1,_ = env.add_free_rectangle(
        (472.5, 365.0), (272.0, 365.0), (271.5, 255.5))
    vert2,_ = env.add_free_rectangle(
        (315.0, 161.0), (216.5, 197.5), (191.0, 129.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(*(vert1+vert2))

def construct_goals(A,B,C,D,E,F,G,H):
    X1 = Point(np.average((A.a,B.a,C.a,D.a), axis = 0))
    X2 = Point(np.average((E.a,F.a,G.a,H.a), axis = 0))
    return line_tool(X1, X2)
