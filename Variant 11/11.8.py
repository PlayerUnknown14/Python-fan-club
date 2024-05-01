from itertools import product
abc = 'ПРИКАЗ'
c = 0

for i in product(abc, repeat=4):
    if i.count('К') == 1:
        c += 1
print(c) #Answer: 500