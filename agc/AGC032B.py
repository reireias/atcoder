#!/usr/bin/env python3

from itertools import combinations

def main():
    n = int(input())
    base = list(range(1, n + 2))
    if n % 2 == 0:
        numbers = [[base[i], base[n-1-i]] for i in range(n // 2)]
    else:
        numbers = [[n]]
        for i in range(n //2):
            numbers.append([base[i], base[n-2-i]])

    result = []
    for first, second in combinations(numbers, 2):
        for fv in first:
            for sv in second:
                result.append((fv, sv))
    print(len(result))
    for r in result:
        print(r[0], r[1])


if __name__ == '__main__':
    main()
