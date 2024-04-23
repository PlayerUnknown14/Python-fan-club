from functools import lru_cache
@lru_cache(None)
def F(n):
    if n < 9:
        return n // 3 + n % 3
    else:
        return F(n // 9) + F(n % 9)
for i in range(0, 9**7 + 100):
    F(i)
c = 0
for n in range(1, 9**7):
    if F(n) == 33:
        c += 1
        print(n)
print(c)