def F(x, y, c):
    if x > y or x == 25 or x == 30 or c >= 2:
        return 0
    if x == y:
        return 1
    return F(x+1, y, 0) + F(x + 2, y, 0) + F(x*3, y, c+1)
print(F(1, 15, 0) * F(15, 43, 0))