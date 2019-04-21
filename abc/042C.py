from collections import defaultdict
N, P = map(int, raw_input().split())
ab = [tuple(map(int, raw_input().split())) for i in xrange(N)]
ab.sort(key=lambda x:x[1], reverse=True)
ab.sort(key=lambda x:x[0], reverse=True)
d = defaultdict(int)
for x in ab:
    for k, v in d.items():
        if k <= P:
            if d[k + x[0]] < v + x[1]:
                d[k + x[0]] = v + x[1]
    if d[x[0]] < x[1]:
        d[x[0]] = x[1] 
print max(d.values())
