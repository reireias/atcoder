import math
N = int(raw_input())
A = map(int, raw_input().split())
P = 10 ** 9 + 7
count = [0] * (max(A) + 1)
for a in A:
    count[a] += 1
if A[0] != 0 or count[0] != 1:
    print 0
    exit(0)

result = 1
for i in xrange(len(count)-1):
    x = count[i]
    y = count[i+1]
    result *= (pow(2**x - 1, y, P) * pow(2, y * (y-1) / 2, P)) % P
print result % P


    
