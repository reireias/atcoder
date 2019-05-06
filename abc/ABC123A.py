#!/usr/bin/env python3


def main():
    points = [int(input()) for _ in range(5)]
    k = int(input())

    exist = points[4] - points[0] > k

    if exist:
        print(':(')
    else:
        print('Yay!')


if __name__ == '__main__':
    main()
