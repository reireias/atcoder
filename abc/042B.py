import math
def dotDist(a, b, c, x, y):

    return abs(a*x + b*y + c) / math.sqrt(a * a + b * b)

def distance(x1, y1, x2, y2, x3, y3):
    L = dotDist(y2-y1, x1-x2, x2*y1-x1*y2, x3, y3)
    return L


x, y = map(int, raw_input().split())
N = int(raw_input())
V = [tuple(map(int, raw_input().split())) for i in xrange(N)]
D = []
for i in xrange(N):
    d = distance(V[i-1][0], V[i-1][1], V[i][0], V[i][1], x, y)
    D.append(d)
print min(D)
