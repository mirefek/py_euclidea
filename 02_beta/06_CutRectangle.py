from constructions import *

def init(env):
    (A,B,C,D), _ = env.add_free_rectangle(
        (433.0, 345.5), (229.0, 345.5), (229.0, 217.0))
    X = env.add_free(511.0, 113.0)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "intersection",
    )
    env.goal_params(A, B, C, D, X)

def construct_goals(A, B, C, D, X):
    Y = Point((A.a+B.a+C.a+D.a)/4)
    return line_tool(X,Y)
