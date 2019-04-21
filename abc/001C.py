import sys
import itertools


def isValid(qx):
    for x in xrange(8):
        if x not in qx:
            return False
    for (i, _i) in itertools.product(xrange(8), repeat=2):
        if i == _i:
            continue
        if qx[i] == qx[_i]:
            return False
        if abs(i - _i) == abs(qx[i] - qx[_i]):
            return False
    return True

board = [sys.stdin.readline().strip() for i in xrange(8)]
qx = [board[y].index('Q') if 'Q' in board[y] else -1 for y in xrange(8)]
sx = [y for y in xrange(8) if qx[y] is -1]
sy = [y for y in xrange(8) if y not in qx]
for ny in itertools.product(sy, repeat=5):
    for i, x in enumerate(ny):
        qx[sx[i]] = x
    if isValid(qx):
        for x in qx:
            print '%sQ%s' % ('.' * x, '.' * (7 - x))
        break
else:
    print 'No Answer'
