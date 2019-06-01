#!/usr/bin/env python3
import sys
sys.setrecursionlimit(1000000)

n = int(input())
d = [0] * n
a = []
b = []
connected = [[] for _ in range(n)]
for i in range(n - 1):
    ai, bi = list(map(int, input().split()))
    d[ai-1] += 1
    d[bi-1] += 1
    a.append(ai-1)
    b.append(bi-1)
    connected[ai-1].append(bi-1)
    connected[bi-1].append(ai-1)
# 次数
c = list(map(int, input().split()))
parents = [-1] * n
result = [0] * n
sortedc = sorted(c, reverse=True)

def dfs(current, parent):
    parents[current] = parent
    parent = parents[current]
    for i in connected[current]:
        if i != parent:
            dfs(i, current)

# 深さ+次数優先
def ddfs(current):
    result[current] = sortedc.pop(0)
    nexts = []
    for i in connected[current]:
        if parents[current] != i:
            nexts.append((i, d[i]))
    sortedNexts = sorted(nexts, reverse=True, key=lambda x: x[1])

    for nxt, _ in sortedNexts:
        ddfs(nxt)

def main():

    dandi = []
    for i, di in enumerate(d):
        dandi.append((i, di))
    sortedd = sorted(dandi, reverse=True, key=lambda x: x[1])

    root = sortedd[0][0]
    dfs(root, -1)
    ddfs(root)

    resultSum = 0
    for i in range(n-1):
        resultSum += min(result[a[i]], result[b[i]])
    print(resultSum)
    print(' '.join(map(str, result)))



if __name__ == '__main__':
    main()
