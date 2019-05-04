#!/usr/bin/env python3

from math import log2

def func(n):
    # (2x) ^ (2x+1) = 1 の性質を利用
    # n = 2mのとき
    # 0^1^...^2m = (0^1) ^ (2^3) ^ ... ^ (2m-2- ^ 2m-1) ^ 2m
    # = 1^...^1 ^ 2m (1はm個)

    # n = 2m+1 のとき
    # 0^1^...^2m+1 = (0^1)^...(2m ^ 2m+1)
    # = 1^...^1 (1は m+1個)

    if n % 2 == 0:
        m = n // 2
        if m % 2 == 0:
            return n
        else:
            return n ^ 1
    else:
        m = (n-1) // 2
        return 0 if m % 2 == 1 else 1

def main():
    a, b = list(map(int, input().split()))

    #f(a, b) = f(0, a-1) ^ f(0, b)
    # f(0, n)をfunc(n)とする
    print(func(b) ^ func(a-1))

if __name__ == '__main__':
    main()
