def no_answers():
    print 'No answers'
    quit()

def another_group(group):
    return group + 1 if group % 10 == 0 else group - 1

N = int(raw_input())
S = [raw_input() for i in xrange(N)]
Word = [raw_input().split() for i in xrange(N)]
r = {}
cnt = 0

for i, w in enumerate(Word):
    x = S[i]
    y = w[0]
    if w[3] == 'bad':
        if x == y:
            no_answers()
        if x not in r and y not in r:
            r[x] = cnt * 10
            r[y] = cnt * 10 + 1
            cnt += 1
        elif x not in r:
            r[x] = another_group(r[y])
        elif y not in r:
            r[y] = another_group(r[x])
        elif r[x] == r[y]:
            no_answers()
        elif abs(r[x] - r[y]) != 1:
            ya = r[y]
            yb = another_group(r[y])
            xa = r[x]
            xb = another_group(r[x])
            for k, v in r.items():
                if v == ya:
                    r[k] = xb
                elif v == yb:
                    r[k] = xa

for i, w in enumerate(Word):
    x = S[i]
    y = w[0]
    if w[3] == 'good':
        if x not in r and y not in r:
            r[x] = r[y] = cnt * 10
            cnt += 1
        elif x not in r:
            r[x] = r[y]
        elif y not in r:
            r[y] = r[x]
        elif abs(r[x] - r[y]) == 1:
            no_answers()
        elif r[x] != r[y]:
            subtgt = another_group(r[y])
            subtgtTo = another_group(r[x])
            for k, v in r.items():
                if v == r[y]:
                    r[k] = r[x]
                elif v == subtgt:
                    r[k] = subtgtTo

rc = {}
for k, v in r.items():
    if v not in rc:
        rc[v] = [k]
    else:
        rc[v].append(k)
honest = []
for i in xrange(cnt):
    a = i * 10
    b = i * 10 + 1
    lena = lenb = 0
    if a in rc:
        lena = len(rc[a])
    if b in rc:
        lenb = len(rc[b])
    if lena > 0 or lenb > 0:
        if lena > lenb:
            honest.extend(rc[a])
        elif lena == lenb:
            mina = min(rc[a])
            minb = min(rc[b])
            if mina < minb:
                honest.extend(rc[a])
            else:
                honest.extend(rc[b])
        else:
            honest.extend(rc[b])
honest.sort()
for i, w in enumerate(Word):
    x = S[i]
    y = w[0]
    if w[3] == 'bad':
        if x in honest and y not in honest:
            continue
        elif y in honest and x not in honest:
            continue
    else:
        if x in honest and y in honest:
            continue
        elif x not in honest and y not in honest:
            continue
    no_answers()
print '\n'.join(honest)

