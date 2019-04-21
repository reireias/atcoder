#!/usr/bin/env python3

from functools import reduce


def main():
    n, a, b = map(int, input().split())
    result = 0
    for num in range(1, n + 1):
        digit_sum = reduce(lambda x, y: x + int(y), str(num), 0)
        if a <= digit_sum and digit_sum <= b:
            result += num
    print(result)


if __name__ == '__main__':
    main()
