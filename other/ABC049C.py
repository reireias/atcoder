#!/usr/bin/env python3

DREAM_PATTERN = ['dream', 'dreamdre', 'dreamera']
DREAMER_PATTERN = ['dreamer', 'dreamerd', 'dreamere']


def daydream(original):
    string = original
    # remove dream and dreamer
    index = string.find('d')
    while index != -1:
        substr = string[index:index + 8]
        if substr in DREAM_PATTERN:
            string = string[:index] + string[index + len('dream'):]
        elif substr in DREAMER_PATTERN:
            string = string[:index] + string[index + len('dreamer'):]
        else:
            return False
        index = string.find('d')

    # remove eraser
    string = string.replace('eraser', '')
    # remove erase
    string = string.replace('erase', '')
    return len(string) == 0


def main():
    s = input()
    if daydream(s):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
