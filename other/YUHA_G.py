import math
def inpolygon(V, point):
    cn = 0
    for i in range(len(V)):
        if (V[i - 1][1] <= point[1] and V[i][1] > point[1]) or (V[i - 1][1] > point[1] and V[i][1] <= point[1]):
            vt = (point[1] - V[i - 1][1]) / (V[i][1] - V[i - 1][1])
            if point[0] < (V[i - 1][0] + (vt * (V[i][0] - V[i - 1][0]))):
                cn += 1
    return cn % 2 == 1

N = int(input())
S = []
P = []
for i in range(N):
    line = input().split()
    S.append(line[0])
    P.append((int(line[1]), int(line[2])))
M = int(input())
T = [input() for i in range(M)]
inside = []
V = []
for t in T:
    V.append(P[S.index(t)])

for i in range(N):
    if S[i] in T:
        continue
    
    if inpolygon(V, P[i]) == True:
        inside.append((P[i][0], i))

inside.sort()
for x in inside:
    print(S[x[1]])

