N, M = map(int, raw_input().split())
R = [0] * (N + 1)
C = []
for i in xrange(M):
    s, t = map(int, raw_input().split()) 
    C.append((s - 1, t - 1))
    R[s - 1] += 1
    R[t] -= 1
for i in xrange(1, N + 1):
    R[i] += R[i - 1]
L = [0] * N
count = 0
for i in xrange(N):
    if R[i] > 1:
        count += 1
        L[i] = count
    else:
        count = 0

r = []
for i in xrange(M):
    if L[C[i][1]] >= C[i][1] - C[i][0] + 1:
        r.append(i+1)
print len(r)
for x in r:
    print x
