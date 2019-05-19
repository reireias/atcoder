#!/usr/bin/env python3


def main():
    n, q = map(int, input().split())
    s = input()
    x = [0] * n
    if s[0:2] == 'AC':
        x[0] = 1
    for i in range(n - 1):
        if s[i+1:i+3] == 'AC':
            x[i+1] = x[i] + 1
        else:
            x[i+1] = x[i]

    for _ in range(q):
        li, ri = map(int, input().split())
        li -= 1
        ri -= 1
        lsum = 0 if li == 0 else x[li-1]
        rsum = x[ri-1]
        print(rsum - lsum)

if __name__ == '__main__':
    main()
