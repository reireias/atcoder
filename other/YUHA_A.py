N = int(raw_input())
L = [raw_input().split() for i in xrange(N)]

result = ''
for l in L:
    if l[0] == 'BEGINNING':
        result += l[2][0]
    elif l[0] == 'MIDDLE':
        result += l[2][len(l[2])/2]
    else:
        result += l[2][-1]
print result
