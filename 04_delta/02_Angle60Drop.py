from constructions import *

def init(env):
    X = env.add_free(360.0, 200.5)
    l = env.add_free_line((8.0, 285.5), (615.5, 289.0))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(X, l)

def construct_goals(X, l):
    normals = (rotate_vector(l.n, ang) for ang in (-np.pi/3, np.pi/3))
    return tuple(
        (Line(n, np.dot(X.a, n)),)
        for n in normals
    )

def additional_bb(X, l, goal):
    return intersection_tool(l, goal)
