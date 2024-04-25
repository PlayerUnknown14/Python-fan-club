from ipaddress import ip_network

net = ip_network('202.75.38.176/255.255.255.240', strict=False)
bin_addresses = [f'{address:b}' for address in net]
c=0
for i in bin_addresses:
    if '111' not in i and '000' not in i:
        c += 1
print(c) #Answer: 5