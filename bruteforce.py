from constructions import *
from environment import load_level
import itertools

def swap_list(l, i, j):
    l[i], l[j] = l[j], l[i]

class BruteForceEnv:
    def __init__(self, env):
        goal = env.goals[0]
        self.goal_p = list(p for p in goal if isinstance(p, Point))
        self.goal_ps = list(ps for ps in goal if isinstance(ps, PointSet))
        self.goal_p_num = len(self.goal_p)
        self.goal_ps_num = len(self.goal_ps)
        self.points = []
        self.point_sets = []
        for obj in env.objs:
            if isinstance(obj, Point):
                self.add_point(obj)
            else:
                assert(isinstance(obj, PointSet))
                self.add_point_set(obj)

    def add_point_set(self, ps):
        # check for duplicity
        if not isinstance(ps, Line) or type(ps) == Line:
            for ps2 in self.point_sets:
                if ps.identical_to(ps2):
                    if not isinstance(ps2, Line) or type(ps2) == Line:
                        return False

        # add intersections
        for ps2 in self.point_sets:
            try:
                for p in singleton_to_tuple(intersection_tool(ps, ps2)):
                    self.add_point(p)
            except:
                pass

        for i in range(self.goal_ps_num):
            if ps.identical_to(self.goal_ps[i]):
                self.goal_ps_num -= 1
                swap_list(self.goal_ps, i, self.goal_ps_num)
                break
        self.point_sets.append(ps)
        return True

    def add_point(self, p):
        for p2 in self.points:
            if p.identical_to(p2): return False

        for i in range(self.goal_p_num):
            if p.identical_to(self.goal_p[i]):
                self.goal_p_num -= 1
                swap_list(self.goal_p, i, self.goal_p_num)
                break
        self.points.append(p)
        return True

    def search(self, limit):
        if self.goal_ps_num == 0 and self.goal_p_num == 0: return ()
        if limit <= 0: return None
        if limit < self.goal_ps_num: return None

        # try lines, circles and perpendicular bisectors
        for (i1,p1),(i2,p2) in itertools.combinations(enumerate(self.points), 2):
            result = self.try_add(line_tool(p1, p2), limit-1, (i1,i2,Line))
            if result is not None: return result
            result = self.try_add(circle_tool(p1, p2), limit-1, (i1,i2,Circle))
            if result is not None: return result
            result = self.try_add(circle_tool(p2, p1), limit-1, (i2,i1,Circle))
            if result is not None: return result
            if all_steps:
                result = self.try_add(perp_bisector_tool(p1, p2), limit-1, (i1,i2,"perp_bisector"))
                if result is not None: return result

        if all_steps:
            # try perpendicular and parallel lines
            for ips,ps in enumerate(self.point_sets):
                if not isinstance(ps, Line): continue
                for ip,p in enumerate(self.points):
                    result = self.try_add(perp_tool(ps, p), limit-1, (ips,ip,"perpendicular"))
                    if result is not None: return result
                    result = self.try_add(parallel_tool(ps, p), limit-1, (ips,ip,"parallel"))
                    if result is not None: return result
            # try angle bisectors
            for (i1,p1),(i2,p2),(i3,p3) in itertools.combinations(enumerate(self.points), 3):
                result = self.try_add(angle_bisector_tool(p1, p2, p3), limit-1,
                                      (i1,i2,i3,"angle_bisector"))
                if result is not None: return result

        return None

    def try_add(self, new_ps, new_limit, info):
        backup = (
            self.goal_p_num,
            self.goal_ps_num,
            len(self.points),
            len(self.point_sets),
        )

        if not self.add_point_set(new_ps): return None
        result = self.search(new_limit)
        #print('try_add inside', result)

        (
            self.goal_p_num,
            self.goal_ps_num,
            p_len,
            ps_len,
        ) = backup
        del self.points[p_len:]
        del self.point_sets[ps_len:]

        if result is None: return None
        else: return (info,)+result

all_steps = False
env = load_level("euclitest", "01_svrk")
#env.objs.extend(env.goals[0][:3])
bf = BruteForceEnv(env)
for p in bf.points:
    print(p)
#l = line_tool(bf.points[1], bf.points[4])
#print('try_add', bf.try_add(l, 0, (1,4,Line)))
print('search', bf.search(4))
