from constructions import *

def rand_init(circ):
    a = np.random.random()*2*np.pi
    r = circ.r * np.random.uniform(np.sqrt(0.5), 0.95)
    return circ.c + r * unit_vector(a)

def init(env):
    circ = env.add_free_circ(
        (319.0, 245.5), 134.3, hidden_center = False)
    X = env.add_free(395.5, 168.5, rand_init = False)
    env.add_rand_init(X, rand_init, (circ,))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(circ, X)

def construct_goals(circ, X):
    C = Point(circ.c)
    X2 = rotate_about_point(X, C, np.pi/2)
    result = []
    for A in intersection_tool(circle_by_diameter(X, X2), circ):
        vertices = [
            rotate_about_point(A, C, np.pi/2*i)\
            for i in range(1,4)
        ]
        result.append([
            segment_tool(*endpoints)
            for endpoints in zip([A]+vertices, vertices+[A])
        ])
    return result
