for A in range(1000):
    c = 0
    for x in range(1000):
        if (((x % 2 == 0) <= (not(x % 13 == 0))) or (x + A >= 1000))==1:
            c += 1
    if c == 999:
        print(A)
        break #Answer: 974