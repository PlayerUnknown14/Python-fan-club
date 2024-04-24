for N in range (100):
    sum = 0
    n = bin(N)[2:]
    m = int(n)
    for i in range(len(n)):
        sum += m % 10
        m = m // 10
    m = int(n)
    if sum % 2 == 1:
        n += '11'
    else:
        n = '11' + n
    R = int(n, 2)
    if R > 102:
        print(N)