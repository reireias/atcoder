#!/usr/bin/env python3


def main():
    costs = [int(input()) for _ in range(5)]
    mods = [cost % 10 for cost in costs if cost % 10 != 0]

    real_cost = []
    for cost in costs:
        if cost % 10 != 0:
            real_cost.append(cost + 10 - (cost % 10))
        else:
            real_cost.append(cost)
    total = sum(real_cost)
    if len(mods) != 0:
        min_mod = min(mods)
        print(total - (10 - min_mod))
    else:
        print(total)


if __name__ == '__main__':
    main()
