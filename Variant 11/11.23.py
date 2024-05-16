<<<<<<< HEAD
def F(x, y):
    if x > y or x == 25 or x == 30:
        return 0
    if x == y:
        return 1
    else:
        return F(x + 1, y) + F(x + 2, y) + F(x * 3, y)
print(F(1, 15) * F(15, 43))
=======
def F(x, y, c):
    if x > y or x == 25 or x == 30 or c >= 2:
        return 0
    if x == y:
        return 1
    return F(x+1, y, 0) + F(x + 2, y, 0) + F(x*3, y, c+1)
print(F(1, 15, 0) * F(15, 43, 0))
>>>>>>> 1d1f62cb83b9c2511b3cef6f66f3decc4f9b9b51
