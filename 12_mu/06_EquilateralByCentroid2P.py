from constructions import *
import itertools

def init(env):
    X = env.add_free(216.5, 284.0)
    Y = env.add_free(453.0, 335.0)
    O = env.add_free(319.0, 245.5)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(X, Y, O)

def construct_goals(X, Y, O):
    ang = 2*np.pi/3
    result = []
    for shift in (-1,1):
        lines = []
        for i in range(3):
            X_cur = rotate_about_point(X, O, i*ang)
            Y_cur = rotate_about_point(Y, O, (i+shift)*ang)
            lines.append(line_tool(X_cur, Y_cur))
        result.append(lines)
    return result

def additional_bb(X,Y,O,goal):
    return [
        intersection_tool(l1, l2)
        for l1, l2 in itertools.combinations(goal, 2)
    ]
        
