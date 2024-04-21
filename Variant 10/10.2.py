for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((x <= y) or (z==x)) and (w <= z)) == 1:
                    print(z, w, x, y)
                elif (((x <= y) or (z==x)) and (w <= z)) == 0:
                    print('FALSE', z, w, x, y) #Answer: zwxy