#!/usr/bin/env python3

import re

def main():
    s = input()
    substrs = re.split('[^ACGT]', s)
    print(max(list(map(len, substrs))))


if __name__ == '__main__':
    main()
