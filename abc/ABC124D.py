#!/usr/bin/env python3

from itertools import accumulate


def main():
    n, k = map(int, input().split())
    s = input()

    # 配列を下記で変換
    # '11000' = [2, 3, 0]
    # '1'の長さで始まり、'1'の長さで終わるようにする
    s = s.replace('01', '0,1').replace('10', '1,0')
    len_list = [len(string) for string in s.split(',')]
    if s[0] == '0':
        len_list = [0] + len_list
    if s[-1] == '0':
        len_list = len_list + [0]

    if 2 * k + 1 >= len(len_list):
        print(n)
        return

    sum_list = [0] + list(accumulate(len_list))
    max_len = 0
    for i in range(0, len(len_list) - (2 * k + 1) + 1, 2):
        handstand_len = sum_list[i + (2 * k + 1)] - sum_list[i]
        if max_len < handstand_len:
            max_len = handstand_len
    print(max_len)


if __name__ == '__main__':
    main()
