from ipaddress import ip_network

net = ip_network("202.75.38.160/255.255.255.240", strict=False)

bin_adresses = [f"{address:b}" for address in net]

c = 0
for address in bin_adresses:
    if "111" in address:
        c += 1
print(c)