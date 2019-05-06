#!/usr/bin/env python3


def main():
    s = input()
    start_0_invalid = 0
    start_1_invalid = 0
    for i, si in enumerate(s):
        if i % 2 == 0:
            if si == '0':
                start_1_invalid += 1
            else:
                start_0_invalid += 1
        else:
            if si == '0':
                start_0_invalid += 1
            else:
                start_1_invalid += 1
    print(min([start_0_invalid, start_1_invalid]))


if __name__ == '__main__':
    main()
