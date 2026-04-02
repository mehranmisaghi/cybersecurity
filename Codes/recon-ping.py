from scapy.all import IP, ICMP, sr, conf

conf.verb = 0

IPs = []

for ip in range(1, 255):
    IPs.append("192.168.0." + str(ip))

pacote = IP(dst=IPs) / ICMP()
ans, unans = sr(pacote, inter=0.1, timeout=1)

print("Hosts ativos")

for enviado, recebido in ans:
    print(recebido[IP].src)

# Para determinar os hosts inativos:
print("Hosts inativos")
for pacoteNaoRecebido in unans:
    print(pacoteNaoRecebido[IP].dst)
