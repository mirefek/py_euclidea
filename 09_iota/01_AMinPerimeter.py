from constructions import *

def init(env):
    A, ray1, ray2 = env.add_free_angle(
        (156.5, 286.5), (547.0, 26.0), (585.0, 286.5))
    X = env.add_free(357.5, 214.0, rand_init = False)
    env.add_rand_init(X, random_point_in_angle, (ray1, ray2))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A, ray1, ray2, X)

def construct_goals(A, ray1, ray2, X):
    X2 = reflect_by_line(X, ray1)
    X3 = reflect_by_line(X2, ray2)
    Y = intersection_tool(line_tool(X,X3), ray2)
    Z = intersection_tool(line_tool(Y,X2), ray1)
    return (
        segment_tool(X, Y),
        segment_tool(Y, Z),
        segment_tool(Z, X),
    )
