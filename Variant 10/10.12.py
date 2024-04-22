from itertools import product
for n in range(1, 1000):
    s = '>' + 21*'0' + n*'1' + 11*'2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace ('>1', '22>')
        if '>2' in s:
            s = s.replace ('>2', '2>')
        if '>0' in s:
            s = s.replace ('>0', '1>')
    s = s.replace('>', '0')
    s = int(s)
    sum = 0
    for i in range(len(str(s))):
        sum += s % 10
        s = s // 10
    if sum % n == 0:
        print(n) #Asnwer: 43
                 #Programm keep writing "1" in terminal. Idk how to fix that