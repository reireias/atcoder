L = str(raw_input()).split(' ')
N = int(L[0])
A = int(L[1])
B = int(L[2])
S = []
D = []
for i in range(N):
    L = str(raw_input()).split(' ')
    S.append(L[0])
    D.append(int(L[1]))

now = 0
for i in range(N):
    x = D[i]
    if x < A:
        x = A
    if B < x:
        x = B

    if S[i] == 'West':
        x *= -1
    now += x
direct = 'West' if now < 0 else 'East'
if now == 0:
    print 0
else:
    print direct, abs(now)


