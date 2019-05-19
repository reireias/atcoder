#!/usr/bin/env python3

import sys
sys.setrecursionlimit(1000000)

n = int(input())
link = [[] for _ in range(n)]
for i in range(n-1):
    ut, vt, wi = list(map(int, input().split()))
    ui = ut - 1
    vi = vt - 1
    link[ui].append((vi, wi))
    link[vi].append((ui, wi))
color = [-1] * n

def dfs(index, c):
    color[index] = c
    for nxt, w in link[index]:
        if color[nxt] == -1:
            dfs(nxt, ((w % 2) + c) % 2)

def main():
    dfs(0, 0)
    for c in color:
        print(c)


if __name__ == '__main__':
    main()
