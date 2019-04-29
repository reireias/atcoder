#!/usr/bin/env python3


def main():
    n = int(input())
    b = list(map(int, input().split()))

    result = []
    for j in range(n):
        for i in range(n - j, 0, -1):
            if b[i-1] == i:
                result.append(i)
                del b[i-1]
                break
    if len(result) == n:
        result.reverse()
        for v in result:
            print(v)
    else:
        print(-1)


if __name__ == '__main__':
    main()
