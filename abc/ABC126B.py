#!/usr/bin/env python3


def main():
    s = input()
    first = int(s[:2])
    last = int(s[2:])

    if first == 0 or first > 12:
        if last >= 1 and last <= 12:
            print('YYMM')
            return
        else:
            print('NA')
            return
    else:
        # first = 1 ~ 12
        if last >= 1 and last <= 12:
            print('AMBIGUOUS')
            return
        else:
            print('MMYY')
            return

if __name__ == '__main__':
    main()
