import Queue
import itertools
N = int(raw_input())
S = [raw_input() for i in xrange(N)]
M = int(raw_input())
Bridge = [tuple(raw_input().split()) for i in xrange(M)]
start = raw_input()
goal = raw_input()
edge = [[0 for i in xrange(N)] for j in xrange(N)]
for x in Bridge:
    a = S.index(x[0])
    b = S.index(x[1])
    edge[a][b] = 1
    edge[b][a] = 1

# remove zero degree
flag = True
while flag:
    removes = []
    for i, x in enumerate(edge):
        if sum(x) == 1:
            removes.append(i)
            flag = True
    if len(removes) == 0:
        flag = False
    for x in removes:
        for i in xrange(N):
            edge[i][x] = 0
            edge[x][i] = 0
    
road = []
si = S.index(start)
gi = S.index(goal)

def checkRoad(x, y):
    lx = []
    for i in xrange(len(x)-1):
        lx.append((min([x[i], x[i+1]]), max([x[i], x[i+1]])))
    ly = []
    for i in xrange(len(y)-1):
        ly.append((min([y[i], y[i+1]]), max([y[i], y[i+1]])))
    sx = set(lx)
    sy = set(ly)
    return len(sx.intersection(sy)) == 0

def getRoute(x, y):
    s = ''
    for i in x:
        s += S[i]
    z = list(reversed(y))
    for i in z[1:len(z)-1]:
        s += S[i]
    return s

def test(qset, now):
    while not qset[now].empty():
        l = qset[now].get()
        i = l[-1]
        rest = set(range(N)).difference(set(l))
        for j, v in enumerate(edge[i]):
            if v == 1 and j in rest:
                newl = list(l)
                newl.append(j)
                if j == gi:
                    road.append(newl)
                else:
                    qset[now + 1].put(newl)

    if qset[now + 1].qsize() == 0:
        return
    test(qset, now + 1)

qset = [Queue.Queue() for i in xrange(N)]
for i, x in enumerate(edge[si]):
    if x == 1:
        if i == gi:
            road.append([si, i])
        else:
            qset[0].put([si, i])

test(qset, 0)
minRoadLength = 2 * N
minRoad = ''
for p, r in itertools.combinations(road, 2):
    length = len(p) + len(r) - 3
    if length > minRoadLength:
        continue
    if checkRoad(p, r):
        if length < minRoadLength:
            minRoadLength = length
            minRoad = min([getRoute(p, r), getRoute(r, p)])
        elif length == minRoadLength:
            m = min([getRoute(p, r), getRoute(r, p)])
            if m < minRoad or minRoad == '':
                minRoad = m
#if minRoad == '' or minRoadLength == N:
#    a = []
#    print a[0]
print minRoad

