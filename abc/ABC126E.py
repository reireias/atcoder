#!/usr/bin/env python3

import sys
sys.setrecursionlimit(1000000)

def get_root(start, parents):
    if parents[start] == -1:
        return start
    else:
        return get_root(parents[start], parents)

def main():
    n, m = list(map(int, input().split()))
    parents = [-1] * (n + 1)
    for _ in range(m):
        x, y, z = list(map(int, input().split()))
        if parents[x] == -1 and parents[y] == -1:
            parents[y] = x
        elif parents[x] == -1:
            root_y = get_root(y, parents)
            if root_y != x:
                parents[x] = y
        elif parents[y] == -1:
            root_x = get_root(x, parents)
            if root_x != y:
                parents[y] = x
        else:
            root_x = get_root(x, parents)
            root_y = get_root(y, parents)
            if root_x != root_y:
                parents[root_y] = root_x
    print(len([0 for p in parents[1:] if p == -1]))


if __name__ == '__main__':
    main()
