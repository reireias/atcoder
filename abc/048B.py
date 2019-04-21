#!/usr/bin/python3

n = int(input())
# win , lose, draw
data = [0] * n
result = [[0, 0, 0] for i in range(n)]
rate = [0] * 100001
hand = [[0, 0, 0] for i in range(100001)]
for i in range(n):
    r, h = map(int, input().split())
    rate[r] += 1
    data[i] = [r, h]
    hand[r][h-1] += 1

for i in range(1, 100001):
    rate[i] += rate[i-1]

for i in range(n):
    r, h = data[i]
    win = rate[r - 1] + hand[r][h % 3]
    draw = hand[r][h - 1] - 1
    lose = n - win - draw - 1
    print(win, lose, draw)

