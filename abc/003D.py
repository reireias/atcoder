import itertools
from collections import defaultdict
from heapq import heappop, heappush
N, M, K = map(int, raw_input().split())
pair = [map(int, raw_input().split()) for i in xrange(M)]
print pair
x = list(xrange(N))
print x
e = {}
dic = defaultdict(int)


def shift(x, n):
    y = list(x)
    y.extend(x[:n])
    return y[n:]


def next(x):
    ret = []
    for i in itertools.combinations(xrange(N), 2):
        y = list(x)
        y[i[0]], y[i[1]] = y[i[1]], y[i[0]]

        z = shift(y, y.index(0))
        ret.append(z)
    return ret


def addNext(n, nextList):
    if n == K:
        return None
    for now in nextList:
        if "".join(map(str, now)) not in e:
            e["".join(map(str, now))] = next(now)
        if n == K-1:
            for j in e["".join(map(str, now))]:
                dic["".join(map(str, j))] += 1
        addNext(n + 1, e["".join(map(str, now))])
    return None


def check(d):
    count = 0
    for k, v in d.iteritems():
        for j in pair:
            li = list(map(int, k))
            dx = abs(li.index(j[1]) - li.index(j[0]))
            if dx != 1 and dx != N - 1:
                count += v
    return count

addNext(0, [x])
# print dic
print sum(dic.values())
print check(dic)
