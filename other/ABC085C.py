#!/usr/bin/env python3


def main():
    n, y = map(int, input().split())
    for num10k in range(n + 1):
        for num5k in range(n - num10k + 1):
            num1k = n - num10k - num5k
            if 10000 * num10k + 5000 * num5k + 1000 * num1k == y:
                print(num10k, num5k, num1k)
                return
    print(-1, -1, -1)


if __name__ == '__main__':
    main()
