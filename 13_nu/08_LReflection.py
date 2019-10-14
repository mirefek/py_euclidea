from constructions import *

def init(env):
    A = env.add_free(319.0, 271.0)
    axis = env.add_line(A, env.add_free(608.5, 271.0, hidden = True))
    env.add_constr(perp_tool, (axis,A), Line)
    l = env.add_line(A, env.add_free(453.0, 216.5, hidden = True))

    env.set_tools(
        "move", "point", "line", "intersection",
    )
    env.goal_params(A, axis, l)

def construct_goals(A, axis, l):
    n2 = l.n - axis.n * 2*np.dot(l.n, axis.n)
    return Line(n2, np.dot(n2, A.a))

def additional_bb(A, axis, l, goal):
    A = A.a
    result = A+l.v, A+l.n, A-l.v, A-l.n
    return [Point(coor) for coor in result]
