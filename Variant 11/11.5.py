sum = 0
for N in range (10000, 100000):
    n = ''
    t = int(N)
    while t>0:
        n += str(t%8)
        t = t // 8
    n = n[::-1]
    for i in range(len(n)):
        if int(n[i]) % 2 == 1:
            n = n.replace(n[i], '2')
    n += str(N%8)
    M = int(n, 8)
    
    n = ''
    t = int(M)
    while t>0:
        n += str(t%8)
        t = t // 8
    n = n[::-1]
    for i in range(len(n)):
        if int(n[i]) % 2 == 1:
            n = n.replace(n[i], '2')
    n += str(M%8)
    R = int(n, 8)
    
    if R % 2023 == 0:
        sum += N    
print(sum) #Answer: 197535