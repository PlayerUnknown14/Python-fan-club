from ipaddress import ip_network

net = ip_network("211.48.136.64/255.255.255.224", strict=False)

bin_addresses = [f"{address:b}" for address in net]

c = 0
for address in bin_addresses:
    if int(address) % 100 == 11:
        c += 1
print(c) # Answer: 8