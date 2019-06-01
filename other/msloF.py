#!/usr/bin/env python3

import sys
sys.setrecursionlimit(1000000)

n = int(input())
people = [i for i in range(n)]
a = [[-1] * n for _ in range(n)]
for i in range(n-1):
    ai = input()
    for j, aij in enumerate(ai):
        a[i+1][j] = int(aij)
        a[j][i+1] = (int(aij) + 1) % 2

memo = {}

# startからendの範囲で優勝の可能性があるやつ
def solve(start, end):
    key = (start, end)
    if key in memo:
        return memo[key]
    if start == end:
        return [start]
    elif start + 1 == end:
        if a[start][end] == 1:
            return [start]
        else:
            return [end]
    winable = set()

    # 全勝の存在をチェック
    for i in range(start, end):
        if sum(a[i]) == end - start + 1 - 2:
            return [i]
    for i in range(start+1, end+1):
        left_winable = solve(start, i-1)
        if (start, i-1) not in memo:
            memo[(start, i-1)] = left_winable
        right_winable = solve(i, end)
        if (i, end) not in memo:
            memo[(i, end)] = right_winable
        for l in left_winable:
            for r in right_winable:
                if a[l][r] == 1:
                    winable.add(l)
                else:
                    winable.add(r)
    return list(winable)


def main():
    winable = solve(0, n-1)
    print(len(winable))


if __name__ == '__main__':
    main()
