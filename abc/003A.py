N = int(raw_input())
G = list(raw_input())
dict = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
GPA = [dict[i] for i in G]
ave = float(sum(GPA)) / N
print '%1.14f' % ave
