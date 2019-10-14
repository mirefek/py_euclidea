from constructions import *

def rand_init(circ):
    v = np.random.normal(size = 2)
    v_norm = v / np.linalg.norm(v)
    v += v_norm * circ.r * 1.5
    return circ.c + v

def init(env):
    C1 = env.add_free(216.0, 249.0)
    X = env.add_free(280.5, 204.0)
    circ = env.add_circle(C1, X)
    C2 = env.add_free(415.5, 197.0, rand_init = False)
    env.add_rand_init(C2, rand_init, (circ,))

    env.set_tools(
        "move", "point", "circle", "intersection",
    )
    env.goal_params(C1, X, C2)

def construct_goals(C1, X, C2):
    return compass_tool(C1, X, C2)
