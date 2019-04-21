N = int(raw_input())
S = [raw_input() for i in xrange(N)]
dic = {s: s[::-1] for s in S}
for k, v in sorted(dic.items(), key=lambda x: x[1]):
    print k
