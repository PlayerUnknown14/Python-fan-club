from fnmatch import *

def IsPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
z = 1205500
while z % 311 != 0:
    z += 1
for n in range(z, 10**8, 311):
    if fnmatch(str(n),  '12?5*5??'):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if IsPrime(i) and IsPrime(n // i):
                    print(n, n // 311)
                else:
                    break