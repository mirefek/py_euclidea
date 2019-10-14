from constructions import *

def init(env):
    A = env.add_free(325.5, 258.0)
    X = env.add_free(449.0, 11.0, hidden = True)
    Y = env.add_free(623.0, 126.0, hidden = True)
    Z = env.add_free(578.5, 427.0, hidden = True)
    x = env.add_line(A,X)
    y = env.add_line(A,Y)
    z = env.add_line(A,Z)

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,x,y,z)

def construct_goals(A,in_x,in_y,in_z):
    result = []
    for x,y,z in (in_x,in_y,in_z), (in_y,in_z,in_x), (in_z,in_x,in_y):
        if np.dot(x.n, y.n) >= 0: axis = x.n+y.n
        else: axis = x.n-y.n
        axis /= np.linalg.norm(axis)
        print(np.dot(z.v, axis))
        n = z.n - 2*(axis * np.dot(z.n, axis))
        result.append((Line(n, np.dot(n, A.a)),))
    return result
