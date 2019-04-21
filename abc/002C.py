import itertools
N = int(raw_input())
c = raw_input()
r = len(c)
term = [''.join(s) for s in itertools.product('ABXY', repeat=2)]
for i in term:
    for j in term:
        r = min(r, len(c.replace(i, 'L').replace(j, 'R')))
print r
