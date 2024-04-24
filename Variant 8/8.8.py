N = 0
p = 0
for n in range(3, 9999):
    S = '1' + '2'*n
    while '12' in S or '322' in S or '222' in S:
        if '12' in S:
            S = S.replace ('12', '2', 1)
        if '322' in S:
            S = S.replace ('322', '21', 1)
        if '222' in S:
            S = S.replace ('222', '3', 1)
    s = int(S)
    sum = 0
    for i in range(len(S)):
        sum += s % 10
        s = s // 10
    if sum > p:
        p = sum
    print(n)
print(p)