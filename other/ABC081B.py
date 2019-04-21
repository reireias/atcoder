#!/usr/bin/env python3

def fact_count(number):
    n = number
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count

def main():
    _ = int(input())
    A = map(int, input().split())
    print(min(map(fact_count, A)))


if __name__ == '__main__':
    main()
