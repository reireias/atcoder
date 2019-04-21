def isLeepYear(y):
    if Y % 4 is 0:
        if Y % 100 is 0:
            if Y % 400 is 0:
                return 'YES'
            return 'NO'
        return 'YES'
    return 'NO'

Y = int(raw_input())
print isLeepYear(Y)
