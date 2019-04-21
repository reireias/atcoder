N, M = map(int, raw_input().split())
a = [input() for i in xrange(M)]
a.reverse()

T = [False] * N

l = []
for i in a:
    if T[i-1] == False:
        T[i-1]=True
        l.append(i)
for i, flag in enumerate(T):
    if flag == False:
        l.append(i+1)
for i in l:
    print i
