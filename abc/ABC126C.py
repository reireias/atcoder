#!/usr/bin/env python3

from math import ceil

def main():
    n, k = list(map(int, input().split()))
    # ダイスの目iのとき、表が必要な数の配列
    needs = [0] * (n + 1)
    p = 0
    current = len(bin(k)) - 2
    for i in range(1, n + 1):
        if k > i * 2**(current-1):
            needs[i] = current
        else:
            current -= 1
            needs[i] = current
        if needs[i] <= 0:
            p += 1 / n
        else:
            p += 0.5 ** needs[i] / n
    print(p)


if __name__ == '__main__':
    main()
