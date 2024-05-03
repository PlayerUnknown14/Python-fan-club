def F(x, y):
    if x > y or x == 25 or x == 30:
        return 0
    if x == y:
        return 1
    else:
        return F(x + 1, y) + F(x + 2, y) + F(x * 3, y)
print(F(1, 15) * F(15, 43))