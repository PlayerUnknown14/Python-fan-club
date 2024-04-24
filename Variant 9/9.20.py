def f(x, h):
    if h == 4 and x >= 88:
        return 1
    elif h == 4 and x < 88:
        return 0
    elif x >= 88 and h < 4:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 3, h + 1)
        else:
            return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 3, h + 1)
 
for x in range(1, 88):
    if f(x, 1) == 1:
        print(x) # Answer: 2528