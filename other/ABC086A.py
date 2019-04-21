#!/usr/bin/env python3


def main():
    a, b = map(int, input().split())
    if a % 2 != 0 and b % 2 != 0:
        print('Odd')
    else:
        print('Even')


if __name__ == '__main__':
    main()
