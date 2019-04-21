import sys
import itertools
N, x = map(int, raw_input().split())
X = [0] * N
Y = [0] * N
C = [0] * N
R = [-1] * (N+1)
for i in xrange(N+1):
    R[i] = [-1] * (N+1)
for i in xrange(N-1):
    X[i+1], Y[i+1], C[i+1] = map(int, sys.stdin.readline().split())
    R[X[i+1]][Y[i+1]] = C[i+1]
    R[Y[i+1]][X[i+1]] = C[i+1]
updated = 1
while updated > 0:
    updated = 0
    for a, b in itertools.combinations(xrange(1, N+1), 2):
        if R[a][b] == -1:
            for i in xrange(1, N+1):
                if i == a or i == b:
                    continue
                if R[a][i] != -1 and R[b][i] != -1:
                    updated += 1
                    c = R[a][i] ^ R[b][i]
                    R[a][b] = c
                    R[b][a] = c
count = 0
for i in xrange(1, N+1):
    for j in xrange(i, N+1):
        if i == j:
            continue
        if R[i][j] == x:
            count += 1
print count
