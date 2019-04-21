S = raw_input().split()
l = []
for x in S:
    if x[0] == 'L':
        l.append('<')
    elif x[0] == 'R':
        l.append('>')
    else:
        l.append('A')
print ' '.join(l)
