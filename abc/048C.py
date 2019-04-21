#!/usr/bin/python3
from fractions import gcd
from functools import reduce

n = int(input())
L = [int(input()) for i in range(n)]
m = min(L)
g = reduce(gcd, [x - m for x in L])
print(pow(2, m + (g + 1) // 2, 10 ** 9 + 7))
