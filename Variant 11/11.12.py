for n in range(4, 100):
    s = '3' + n*'7'
    while '37' in s or '577' in s or '777' in s:
        if '37' in s:
            s = s.replace('37', '7', 1)
        if '577' in s:
            s = s.replace('577', '73', 1)        
        if '777' in s:
            s = s.replace('777', '5', 1)
    sum = 0
    S = int(s)
    for i in range(len(s)):
        sum += S % 10
        S = S // 10
    m = 0
    for k in range(2, max(n, sum)):
        if sum % k == 0 and n % k == 0:
            m += 1
    if sum > 9 and sum < 100 and m == 0:
        print(n) #Answer: 97