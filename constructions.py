import numpy as np
from geo_object import *

def rot_args(i, *args):
    return args[i:] + args[:i]

def rots_args(*args):
    return (rot_args(i, *args) for i in range(len(args)))

def singleton_to_tuple(x):
    if isinstance(x, (list, tuple)): return x
    else: return x,

def tuple_to_singleton(x):
    if len(x) == 1: return x[0]
    else: return x

def cpx_to_a(cpx):
    return np.stack((cpx.real, cpx.imag), axis = -1)
def rotate_vector(vec, ang):
    return cpx_to_a(complex(*vec) * np.exp(ang*1j))
def unit_vector(ang):
    return cpx_to_a(np.exp(ang*1j))

def vec_angle(v1, v2):
    cpx1 = complex(*v1)
    cpx2 = complex(*v2)
    return np.angle(cpx2 / cpx1)

def intersection_ll(line1, line2):

    matrix = np.stack((line1.n, line2.n))
    b = np.array((line1.c, line2.c))
    if abs(np.linalg.det(matrix)) < epsilon:
        raise Exception("No line intersection")
    return np.linalg.solve(matrix, b)

def is_intersecting_ll(line1, line2):
    matrix = np.stack((line1.n, line2.n))
    b = np.array((line1.c, line2.c))
    if abs(np.linalg.det(matrix)) < epsilon:
        return False
    X = np.linalg.solve(matrix, b)
    return line1.contains(X) and line2.contains(X)

def intersection_lc(line, circle):
    # shift circle to center
    y = line.c - np.dot(line.n, circle.c)
    x_squared = circle.r_squared - y**2
    if x_squared < -epsilon:
        #print("negative det")
        return []
    if x_squared <= epsilon: x = np.zeros((1,1))
    else:
        x = np.sqrt(x_squared)
        x = np.array(((x,),(-x,)))
    result = x*line.v + y*line.n
    # shift back
    return list(result + circle.c)

def intersection_cc(circle1, circle2):
    center_diff = circle2.c - circle1.c
    center_dist_squared = np.dot(center_diff, center_diff)
    assert(center_dist_squared > epsilon)
    center_dist = np.sqrt(center_dist_squared)
    relative_center = (circle1.r_squared - circle2.r_squared) / center_dist_squared
    center = (circle1.c + circle2.c)/2 + relative_center*center_diff/2

    rad_sum  = circle1.r + circle2.r
    rad_diff = circle1.r - circle2.r
    det = (rad_sum**2 - center_dist_squared) * (center_dist_squared - rad_diff**2)
    if det < -epsilon: return []
    if det <= epsilon: return [center]
    center_deviation = np.sqrt(det)
    center_deviation = np.array(((center_deviation,),(-center_deviation,)))
    center_deviation = center_deviation * 0.5*vector_perp_rot(center_diff) / center_dist_squared

    return list(center + center_deviation)

def intersection_tool(point_set1, point_set2):
    if isinstance(point_set1, Line) and isinstance(point_set2, Line):
        result = intersection_ll(point_set1, point_set2),
    elif isinstance(point_set1, Line) and isinstance(point_set2, Circle):
        result = intersection_lc(point_set1, point_set2)
    elif isinstance(point_set1, Circle) and isinstance(point_set2, Line):
        result = intersection_lc(point_set2, point_set1)
    elif isinstance(point_set1, Circle) and isinstance(point_set2, Circle):
        result = intersection_cc(point_set1, point_set2)
    result = [
        Point(coor)
        if (point_set1.contains(coor) and point_set2.contains(coor)) else None
        for coor in result
    ]
    assert(len(result) > 0)
    if len(result) == 1: result, = result
    return result

def line_tool(point1, point2):
    normal_vector = vector_perp_rot(point1.a - point2.a)
    c = np.dot(normal_vector, point1.a)
    return Line(normal_vector, c)
def perp_tool(line, point):
    return Line(line.v, np.dot(line.v, point.a))
def parallel_tool(line, point):
    return Line(line.n, np.dot(line.n, point.a))
def circle_tool(center, point):
    radius = np.linalg.norm(point.a - center.a)
    return Circle(center.a, radius)
def compass_tool(X, Y, center):
    radius = np.linalg.norm(X.a - Y.a)
    return Circle(center.a, radius)
def segment_tool(A, B):
    return Segment(A.a, B.a)
def ray_tool(A, B):
    return Ray(A.a, B.a-A.a)
def perp_bisector_tool(A, B):
    M = (A.a + B.a)/2
    n = A.a - B.a
    return Line(n, np.dot(M, n))

def angle_bisector_tool(A, B, C):
    v1 = A.a - B.a
    v2 = C.a - B.a
    v1 /= np.linalg.norm(v1)
    v2 /= np.linalg.norm(v2)
    if np.dot(v1, v2) > 0:
        n = vector_perp_rot(v1+v2)
    else:
        n = v1-v2
    return Line(n, np.dot(B.a, n))
def ext_angle_bisector(A, B, C):
    v1 = A.a - B.a
    v2 = C.a - B.a
    v1 /= np.linalg.norm(v1)
    v2 /= np.linalg.norm(v2)
    if np.dot(v1, v2) > 0:
        n = v1+v2
    else:
        n = vector_perp_rot(v1-v2)
    return Line(n, np.dot(B.a, n))
    
def midpoint_tool(A,B):
    return Point((A.a+B.a)/2)
def circumcircle_tool(A,B,C):
    l1 = perp_bisector_tool(A,B)
    l2 = perp_bisector_tool(B,C)
    O = intersection_tool(l1, l2)
    return circle_tool(O,A)
def circle_by_diameter(A,B):
    center = (A.a+B.a)/2
    radius = np.linalg.norm(A.a-center)
    return Circle(center, radius)

def polar_tool(X, circ):
    n = X.a - circ.c
    c = np.dot(n, circ.c) + circ.r**2
    return Line(n, c)
def radical_axis(pc1, pc2):
    if isinstance(pc1, Circle):
        C1, r1 = pc1.c, pc1.r
    elif isinstance(pc1, Point):
        C1, r1 = pc1.a, 0
    else: raise Exception("Unexpected type for radical axis: {}".format(type(pc1)))
    if isinstance(pc2, Circle):
        C2, r2 = pc2.c, pc2.r
    elif isinstance(pc2, Point):
        C2, r2 = pc2.a, 0
    else: raise Exception("Unexpected type for radical axis: {}".format(type(pc2)))

    n = C1-C2
    dist = np.linalg.norm(n)
    coef1 = 0.5 + (r2**2 - r1**2)/(2*dist**2)
    coef2 = 1 - coef1
    M = C1*coef1 + C2*coef2
    return Line(n, np.dot(M, n))

def point_on(coor, obj):
    coor = obj.closest_on(coor)
    return Point(coor)

def intersection_close_to(coor, obj0, obj1):
    intersections = filter(lambda x: x is not None,
                           singleton_to_tuple(intersection_tool(obj0, obj1)))
    return min(intersections, key = lambda p: p.dist_from(coor))

def reflect_by_line(X, line):
    shift = 2*(line.c - np.dot(X.a, line.n))
    return Point(X.a + shift*line.n)
def reflect_by_point(obj, C):
    if isinstance(obj, Point):
        return Point(2*C.a - obj.a)
    elif isinstance(obj, Circle):
        return Circle(2*C.a - obj.c, obj.r)
    elif isinstance(obj, Line):
        return Line(obj.n, 2*np.dot(obj.n, C.a) - obj.c)
    else: raise Exception("Unexpected type: {} of reflected object".format(type(obj)))
        
def rotate_about_point(obj, center, angle):
    if isinstance(obj, Point):
        return Point(center.a + rotate_vector(obj.a-center.a, angle))
    elif isinstance(obj, Circle):
        return Circle(center.a + rotate_vector(obj.c-center.a, angle), obj.r)
    elif isinstance(obj, Line):
        n = rotate_vector(obj.n, angle)
        c = obj.c + np.dot(center.a, n) - np.dot(center.a, obj.n)
        return Line(n, c)
    else: raise Exception("Unexpected type: {} of rotated object".format(type(obj)))
def rotate_ray(ray, angle):
    return Ray(ray.start_point, rotate_vector(ray.v, angle))

def parallelogram(A, B, C):
    D = Point(A.a+C.a-B.a)
    return (
        D,
        Segment(A.a, B.a), Segment(B.a, C.a),
        Segment(C.a, D.a), Segment(D.a, A.a),
    )

def square_vertices(A, B):
    v = vector_perp_rot(B.a - A.a)
    return Point(B.a + v), Point(A.a + v)

def square(A, B):
    C, D = square_vertices(A, B)
    return (
        C, D,
        Segment(A.a, B.a), Segment(B.a, C.a),
        Segment(C.a, D.a), Segment(D.a, A.a),
    )

# random constructions

def random_point():
    return np.random.normal(size = 2)

def random_point_on(obj):
    if isinstance(obj, Circle):
        return obj.r * unit_vector(np.random.random()*2*np.pi) + obj.c
    elif isinstance(obj, Segment):
        offset = 0.1
        coef = np.random.uniform(offset, 1-offset)
        x,y = obj.end_points
        return coef*x + (1-coef)*y
    elif isinstance(obj, Ray):
        return obj.start_point + obj.v * np.random.lognormal()
    else: return obj.closest_on(random_point())

def random_point_in_angle(ray1, ray2):
    assert((ray1.start_point == ray2.start_point).all())
    ang1 = np.angle(complex(*ray1.v))
    ang2 = np.angle(complex(*ray2.v))
    if ang1 > ang2: ang1, ang2 = ang2, ang1
    if ang2 - ang1 > np.pi:
        ang1 += 2*np.pi
    offset = 0.1
    coef = np.random.uniform(offset, 1-offset)
    ang = coef*ang1 + (1-coef)*ang2
    return np.random.lognormal() * unit_vector(ang) + ray1.start_point

def random_point_in_triangle(A,B,C, offset = 0.06):
    ab = np.random.random(size = 2)
    ab.sort()
    a,b = ab*(1-3*offset) + offset
    # a in (o, 1-2o), b in (a, 1-2o)
    b -= a-offset
    # a in (o, 1-2o), b in (o, 1-a-o)
    c = 1-a-b
    # c in (o, 1-2o)
    return a*A.a + B.a*b + C.a*c

def random_point_in_circle(circ, offset = 0.1):
    ra = np.random.random(size = 2)
    ra.sort()
    r,a = ra
    r,a = circ.r * r*(1-offset), (a-r)/(1-r) * 2*np.pi
    r *= (1-offset)
    return circ.c + r * unit_vector(a)

def random_triangle(acute_prob = 0.6):
    angles = np.random.random(size = 3) * np.pi
    angles.sort()
    mode, mode_spec, reflect = np.random.random(size = 3)
    if mode < acute_prob:
        angles[1] -= np.pi
    else:
        if mode_spec < 1/3: angles[0] -= np.pi
        elif mode_spec < 2/3: angles[2] -= np.pi

    if reflect < 0.5: angles += np.pi
    return (
        unit_vector(ang)
        for ang in angles
    )

def random_acute_triangle():
    return random_triangle(1.1)
def random_obtuse_triangle():
    return random_triangle(-0.1)

def random_line():
    return Line(
        unit_vector(np.random.random() * 2*np.pi),
        np.random.normal(),
    )

def random_trapezoid():
    l1,l2 = (random_line() for _ in range(2))
    A,B = (random_point_on(l1) for _ in range(2))
    C,D = (random_point_on(l2) for _ in range(2))
    if np.dot(A-B, C-D) > 0:
        C,D = D,C
    return A,B,C,D

def random_convex_quadrilateral():
    angles = np.random.random(size = 4) * 2*np.pi
    angles.sort()
    cyclic = unit_vector(angles)
    scale = np.sqrt(np.random.lognormal())
    scale = np.array((scale, 1/scale))
    ang = np.random.random() * np.pi/2
    return [rotate_vector(v, ang) for v in cyclic * scale]
