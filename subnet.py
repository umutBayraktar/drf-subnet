import ipaddress

def get_subnets(ip_address, prefix_length):
    ip = ipaddress.ip_interface(f"{ip_address}/{prefix_length}")
    network = ip.network

    subnets = []
    for subnet in network.subnets():
        subnets.append(str(subnet))

    return subnets

# Örnek Kullanım
ip_address = "192.168.0.0"
prefix_length = 24

subnets = get_subnets(ip_address, prefix_length)
print(subnets)
