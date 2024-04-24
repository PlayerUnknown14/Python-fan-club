for i in range (2023, 10**9, 2023):
    sum = 0
    n = i
    for k in range(len(str(i))):
        sum += n % 10
        n = n // 10
    L = len(str(i))
    if (sum % 7 == 0) and (sum < 20) and (str(i)[:2] == '20') and (str(i)[(L-2):(L)] == '23'):
        print(i, i/2023) #Answer: 2023 1.0    204323 101.0    2025023 1001.0    20232023 10001.0    202302023 100001.0