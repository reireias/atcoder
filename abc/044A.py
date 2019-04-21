N = int(raw_input())
if N == 1:
    print 'Not Prime'
elif N in [2, 3, 5]:
    print 'Prime'
elif N % 2 == 0 or N % 3 == 0 or N % 5 == 0:
    print 'Not Prime'
else:
    print 'Prime'
