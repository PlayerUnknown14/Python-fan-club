from ipaddress import ip_network

net = ip_network('158.132.161.128/255.255.255.128', strict=False)

bin_addresses = [f"{address:b}" for address in net]

c = 0
for i in bin_addresses:
    if int(i) % 10 == 1:
        c += 1
print(c) #Answer: 64