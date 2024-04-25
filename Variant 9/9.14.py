list = []
for x in range(12):
    for y in range(19):
        a = 5 * 12**4 + x * 12**3 + 9 * 12**2 + x * 12 + 4
        b = 7 * 14**3 + x * 14**2 + x * 14 + 6
        c = 5 * 16**4 + 5 * 16**3 + x * 16**2 + x * 16 + 8
        d = 3 * 19**3 + y * 19**2 + x * 19 + 7
        e = a + b + c - d
        e1 = True
        for i in range(2, (e//2) + 1):
            if e % i == 2:
                e1 = False
        if e1 == True:
            list.append(x*y)
print(max(list)) #Answer: 170