L = map(int, raw_input().split())
L.sort()
if L[0] == L[1]:
    print L[2]
else:
    print L[0]
