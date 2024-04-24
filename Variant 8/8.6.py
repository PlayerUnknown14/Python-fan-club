from itertools import product
abc = 'ЬРПЛЕА'
n = 0
sum = 0

for i in product(abc, repeat=5):
    n += 1
    if i[4] == 'Ь':
        sum += 1
    if n == 387:
        print(sum); break