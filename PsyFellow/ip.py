from ipaddress import ip_network

net = ip_network('144.12.200.0/255.255.248.0')
c = 0
for ip in net:
    if bin(int(ip)).count('1') % 3 != 0:
        c += 1
print(c)