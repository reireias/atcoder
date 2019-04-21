import itertools

S = list(raw_input())
N = int(raw_input())

D = [x + y for x, y in  itertools.product(S, S)]
D.sort()
print D[N-1]

