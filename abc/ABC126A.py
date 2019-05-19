#!/usr/bin/env python3


def main():
    n, k = list(map(int, input().split()))
    s = input()
    result = ''
    for i, st in enumerate(s):
        if i == k-1:
            result += st.lower()
        else:
            result += st
    print(result)


if __name__ == '__main__':
    main()
