from scapy.all import Ether, ARP, srp, conf

conf.verb = 0

IPs = []

for ip in range(1, 255):
  IPs.append("192.0.2" + str(ip))
  #  IPs.append("teste com endereços da sua rede" + str(ip))

pacoteARP = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=IPs)
ans, unans = srp(pacoteARP, inter=0.1, timeout=1)

print("IP\t\tMAC")

for enviado, recebido in ans:
    print(f"{recebido.psrc}\t{recebido.hwsrc}")
