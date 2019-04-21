T = raw_input().split(" ")
N = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2]
dT = abs(int(T[1]) - int(T[0]))
count = dT / 10
count += N[dT % 10]
print count
