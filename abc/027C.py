import math
N = int(raw_input())
n = 1
p = 1
while N > n:
    p *= 4
    n += p
    if N <= n:
        print 'Takahashi'
        quit()
    n += p
    if N <= n:
        print 'Aoki'
        quit()
else:
    print 'Aoki'

