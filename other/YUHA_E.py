# coding: utf-8
from collections import defaultdict
N = int(raw_input())
S = [raw_input().decode('utf-8') for i in xrange(N)]
LA = [raw_input().decode('utf-8') for i in xrange(5)]
left = u'\u2190'
right = u'\u2192'
up = u'\u2191'
down = u'\u2193'
L = [0] * 4
L[0] = (LA[0][2], LA[1][2] == down)
L[1] = (LA[2][0], LA[2][1] == right)
L[2] = (LA[2][4], LA[2][3] == left)
L[3] = (LA[4][2], LA[3][2] == up)
d = defaultdict(int)
for x in L:
    index = 0 if x[1] else 1
    other = (index + 1) % 2
    for s in S:
        if s[index] == x[0]:
            d[s[other]] += 1
for k, v in d.items():
    if v == 4:
        print k.encode('utf-8')
