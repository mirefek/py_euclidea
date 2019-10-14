from constructions import *

def init(env):
    A = env.add_free(170.5, 249.5)
    C = env.add_free(472.5, 247.0)
    axis = env.add_constr(
        perp_bisector_tool, (A, C), Line,
        hidden = True,
    )
    B = env.add_dep((321.0, 171.0), axis)
    D, *segments = env.add_constr(
        parallelogram, (A,B,C),
        (Point, Line, Line, Line, Line),
    )

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "intersection",
    )
    env.goal_params(A, C, segments[0])

def construct_goals(A, C, seg0):
    center = (A.a+C.a)/2
    return Circle(center, seg0.dist_from(center))
