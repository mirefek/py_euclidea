from constructions import *

def init(env):
    A,B,_ = env.add_free_segment((268.0, 369.0), (397.0, 368.5))

    env.set_tools(
        "move", "point", "line", "circle",
        "perp_bisector", "angle_bisector",
        "perpendicular", "parallel",
        "compass", "intersection",
    )
    env.goal_params(A,B)

def construct_goals(A_in, B_in):
    result = []
    for (A,B) in (A_in.a,B_in.a),(B_in.a,A_in.a):
        v = B - A
        n = vector_perp_rot(v)
        s2 = np.sqrt(0.5)
        C = B + (v+n)*s2
        D = C + n
        E = B + n*(2*s2+1)
        F = A + n*(2*s2+1)
        H = A + (n-v)*s2
        G = H + n
        result.append((
            Segment(B,C),
            Segment(C,D),
            Segment(D,E),
            Segment(E,F),
            Segment(F,G),
            Segment(G,H),
            Segment(H,A),
        ))
    return result
