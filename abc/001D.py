from collections import namedtuple
import math
Point = namedtuple('Point', 'l r')


def slope(sx, sy, gx, gy):
    return float(gx - sx)/float(gy - sy)


def calcLoad(load, sx, sy, gx, gy):
    if gy - sy == 1:
        return math.hypot(sx-gx, sy-gy)
    nowSlope = slope(sx, sy, gx, gy)
    y = [sx + i * nowSlope for i in xrange(gy - sy + 1)]
    out = [i + sy for i, v in enumerate(y) if not load[i + sy].l <= v <= load[i + sy].r]
    if len(out) == 0:
        return math.hypot(sx-gx, sy-gy)
    edge = [load[i].l if y[i] < load[i].l else load[i].r for i in out]
    slopes = [slope(sx, 0, edge[i], v) for i, v in enumerate(out)]
    absSlopes = [abs(i) for i in slopes]
    t = absSlopes.index(max(absSlopes))
    return calcLoad(load, sx, sy, edge[t], out[t])\
        + calcLoad(load, edge[t], out[t], gx, gy)

N = int(raw_input())
start, goal = raw_input().split(' ')

load = [Point._make(map(int, raw_input().split(' '))) for i in xrange(N+1)]
print '%10.14f' % calcLoad(load, int(start), 0, int(goal), N)
