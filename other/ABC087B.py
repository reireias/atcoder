#!/usr/bin/env python3

from itertools import product


def main():
    coin500 = int(input())
    coin100 = int(input())
    coin50 = int(input())
    expect = int(input())
    count = 0
    for c500, c100, c50 in product(range(coin500 + 1), range(coin100 + 1), range(coin50 + 1)):
        if 500 * c500 + 100 * c100 + 50 * c50 == expect:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
