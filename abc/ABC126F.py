#!/usr/bin/env python3


def main():
    m, k = list(map(int, input().split()))
    if k >= 2**m:
        print(-1)
        return
    if m == 0:
        if k == 0:
            print('0 0')
        else:
            print(-1)
        return
    if m == 1:
        if k == 0:
            print('1 0 0 1')
        else:
            print(-1)
        return
    result = [i for i in range(2**m) if i != k]
    b = list(map(str, result))
    c = reversed(b)
    print(' '.join(b), k, ' '.join(c), k)


if __name__ == '__main__':
    main()
