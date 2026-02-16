from ipaddress import ip_network

net = ip_network('206.123.209.193/255.255.252.0', strict=False)
c = 0
for ip in net:
    if bin(int(ip)).count('1') == 15:
        c += 1
print(c)