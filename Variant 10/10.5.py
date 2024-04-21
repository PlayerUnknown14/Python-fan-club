for N in range(100):
    n = bin(N)[2:]
    n = n[::-1]
    n += str(int(n)%10)
    R = int(n, 2)
    if R > 99:
        print(N) # Answer: 39