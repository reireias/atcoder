from heapq import heappush, heappop
N, M = map(int, raw_input().split())
c = [raw_input() for i in xrange(N)]
goal = None
for i in xrange(N):
    j = c[i].find('g')
    if j >= 0:
        goal = (i, j)
        break


def neighbor(p):
    i, j = p
    v = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return filter(lambda p: 0 <= p[0] < N and 0 <= p[1] < M, v)


class State(tuple):
    __lt__ = lambda self, other: self[0] > other[0]


def search(queue):
    best = [[0 for j in range(M)] for i in range(N)]
    while len(queue) > 0:
        v, p = heappop(queue)

        npos = [(i, j) for i, j in neighbor(p)
                if c[i][j] != '#' and c[i][j] != 'g']

        for (i, j) in npos:
            if c[i][j] == 's':
                return v
            nv = min(v * 0.99, float(c[i][j]) * 0.99)
            if nv > best[i][j]:
                best[i][j] = nv
                heappush(queue, State((nv, (i, j))))
    return -1
queue = []
heappush(queue, State((9, goal)))
print search(queue)
