def F(S, h):
    if (h == 5 or h == 3) and S <= 0:
        return 1
    elif h == 5 and S > 0:
        return 0
    elif h < 5 and S <= 0:
        return 0
    else:
        if h % 2 == 0 and S > 5:
            return F(S - 5, h + 1) or F(S // 3, h + 1)
        elif h % 2 == 0 and S <= 5:
            return F(S // 3, h + 1)
        elif h % 2 == 1 and S <= 5:
            return F(S // 3, h + 1)
        else:
            return F(S - 5, h + 1) and F(S // 3, h + 1)

def F1(S, h):
    if h == 3 and S <= 0:
        return 1
    elif h == 3 and S > 0:
        return 0
    elif h < 3 and S <= 0:
        return 0
    else:
        if h % 2 == 0 and S > 5:
            return F1(S - 5, h + 1) or F1(S // 3, h + 1)
        elif h % 2 == 0 and S <= 5:
            return F1(S // 3, h + 1)
        elif h % 2 == 1 and S <= 5:
            return F1(S // 3, h + 1)
        else:
            return F1(S - 5, h + 1) and F1(S // 3, h + 1)

for S in range(100, 1, -1):
    if F(S, 1) == 1:
        print(S)     
print('====')
for S in range(100, 1, -1):
    if F1(S, 1) == 1:
        print(S) #Answer: 28