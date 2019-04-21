S = raw_input()
n = len(S)
now = m = 0
v = []
for i in xrange(n-1, -1, -1):
    if S[i] == '+':
        now += 1
    elif S[i] == '-':
        now -= 1
    else:
        v.append(now)
        m += 1

v.sort()
out = 0
for i in xrange(m/2):
    out -= v[i]
for i in xrange(m/2, m):
    out += v[i]
print out
