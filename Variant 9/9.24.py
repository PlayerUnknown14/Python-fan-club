F = open('24-1.txt')
f = F.readline()
F.close
f = f.split('A')
m = 0
for i in range(len(f)-5):
    ft = 'A'.join(f[i:i+6])
    if m < len(ft):
        m = len(ft)
print(m)