f = open('27-164a.txt')
n, k  = map(int, f.readline().split())
a = [[] for i in range(10001)]
for i in f:
    x, y, z = map(int, i.split())
    a[x].append([y, z])
mx = 0
for Z in a:
    for X in range(len(Z) - 1):
        for C in range(X + 1, len(Z)):
            if abs(Z[X][0] - Z[C][0]) >= k:
                mx = max(mx, abs(Z[X][1] - Z[C][1]))
print(mx) #Answer(a): 898

f = open('27-164b.txt')
n, k  = map(int, f.readline().split())
a = [[] for i in range(10001)]
for i in f:
    x, y, z = map(int, i.split())
    a[x].append([y, z])
mx = 0
for Z in a:
    for X in range(len(Z) - 1):
        for C in range(X + 1, len(Z)):
            if abs(Z[X][0] - Z[C][0]) >= k:
                mx = max(mx, abs(Z[X][1] - Z[C][1]))
print(mx) #Answer(b): 98526430
#Answer: 898 98526430