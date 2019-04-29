#!/usr/bin/env python3


def degree_dict(degrees):
    result = {}
    for v in degrees[1:]:
        if v in result:
            result[v] += 1
        else:
            result[v] = 1
    return result

def get_path_count(a, b, start_node, end_node):
    m = len(a)

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for _ in range(m):
        ai, bi = list(map(int, input().split()))
        a.append(ai)
        b.append(bi)

    # check degree
    degrees = [0] * (n + 1)
    for ai, bi in zip(a, b):
        degrees[ai] += 1
        degrees[bi] += 1
    deg_dict = degree_dict(degrees)
    if len(deg_dict.keys()) != 2:
        print('No')
        return

    if 6 in deg_dict and 2 in deg_dict:
        print('Yes')
        return
    elif 4 in deg_dict and 2 in deg_dict and deg_dict[4] > 2:
        print('Yes')
        return
    elif 4 in deg_dict and 2 in deg_dict and deg_dict[4] == 2:
        nodes = []
        for i, degree in enumerate(degrees):
            if degree == 4:
                nodes.append(i + 1)
        if get_path_count(a, b, nodes[0], nodes[1]) == 2:
            print('Yes')
        else:
            print('No')
        return
    else:
        print('No')
        return


if __name__ == '__main__':
    main()
