#!/usr/bin/env python3

from itertools import product
import sys
sys.setrecursionlimit(100000)

def get_label(labels, target):
    if labels[target] == -1:
        return target
    else:
        temp = get_label(labels, labels[target])
        labels[target] = temp
        return temp


def main():
    n, m = list(map(int, input().split()))
    a = []
    b = []
    for _ in range(m):
        ai, bi = list(map(int, input().split()))
        a.append(ai-1)
        b.append(bi-1)

    # 不便さのMAX
    result = [n * (n-1) // 2]
    labels = [-1] * n
    groups = {}
    for i in range(n):
        groups[i] = 1

    for j in range(m):
        i = m - 1 - j
        ai = a[i]
        bi = b[i]
        label_a = get_label(labels, ai)
        label_b = get_label(labels, bi)
        if label_a != label_b:
            next_val = result[-1]
            next_val -= groups[label_a] * groups[label_b]
            result.append(next_val)
            groups[label_a] += groups[label_b]
            labels[label_b] = label_a
            del groups[label_b]
        else:
            result.append(result[-1])

    result.reverse()
    for v in result[1:]:
        print(v)

if __name__ == '__main__':
    main()
