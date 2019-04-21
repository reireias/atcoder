#!/usr/bin/env python3


def main():
    n = int(input())
    t = [0]
    x = [0]
    y = [0]
    for _ in range(n):
        tt, tx, ty = map(int, input().split())
        t.append(tt)
        x.append(tx)
        y.append(ty)

    # dt = t_i+1 - t とし、
    # (x_i, y_i) と (x_i+1, y_i+1) のマンハッタン距離dが
    # d <= dt and (dt - d) % 2 == 0 なら到達可能
    for i in range(n):
        dt = t[i + 1] - t[i]
        d = abs(x[i] - x[i + 1]) + abs(y[i] - y[i + 1])
        if d > dt or (dt - d) % 2 != 0:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()
