f = open('24-1.txt').readline()
f = 'A' + f + 'A'

index_A = []
for i in range(len(f)):
    if f[i] == 'A':
        index_A.append(i)

len_A = []
for i in range(len(index_A)-6):
    len_A.append(index_A[i + 6] - index_A[i] - 1)

print(max(len_A)) #Answer: 229