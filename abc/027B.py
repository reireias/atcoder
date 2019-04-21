N = int(raw_input())
A = map(int, raw_input().split())
s = sum(A)
if s == 0:
    print 0
    quit()
if s % N != 0:
    print -1
    quit()
M = s / N
total = 0
need = N
for i in xrange(N):
    total += A[i] - M
    if total == 0:
        need -= 1
print need

