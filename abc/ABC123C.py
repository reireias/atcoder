#!/usr/bin/env python3


def main():
    n = int(input())
    sizes = [int(input()) for _ in range(5)]
    min_size = min(sizes)
    if min_size < n:
        if n % min_size == 0:
            times = int(n / min_size)
        else:
            times = int(n / min_size) + 1
        print(5 + times - 1)
    else:
        print(5)


if __name__ == '__main__':
    main()
