Z = 4*(8**3032) + 3*(16**1956) + 870
z= ''
while Z != 0: 
    z += str(Z % 7)
    Z //= 7
z = z[::-1]
print(z.count('3')*3 - z.count('1')*1)