def F(n):
    if n >= 2020:
        return n
    else:
        return n + 2 + F(n+3)
print(F(2012)-F(2023))# Answer: 6049