#!/usr/bin/env python3
 
from fractions import gcd
 
def all_gcd(numbers):
    result = numbers[0]
    for v in numbers:
        result = gcd(result, v)
    return result
 
def main():
    n = int(input())
    a = list(map(int, input().split()))
    # x[i] = gcd 0 to i
    x = []
    for i in range(n):
        prev = 0 if i == 0 else x[i - 1]
        x.append(gcd(a[i], prev))
    # y[i] = gcd i to n
    y = [0] * n
    y[n-1] = a[n-1]
    for i in range(2, n + 1):
        y[n-i] = gcd(y[n-i+1], a[n-i])

    max_gcd = 0
    for i in range(n):
        if i == 0:
            now_gcd = y[1]
        elif i == n-1:
            now_gcd = x[n-2]
        else:
            now_gcd = gcd(x[i-1], y[i+1])
        if now_gcd > max_gcd:
            max_gcd = now_gcd
    print(max_gcd)
 
if __name__ == '__main__':
    main()
