from scapy.all import *
conf.verb = 0

host = "seu ip"
# host = "teste com o endereço do host que deseja escanear"
portas = [22, 80, 666, 12345]
# 80 é a porta do HTTP, 22 é a porta do SSH, 666 é uma porta geralmente usada por malwares.
# 12345 é uma porta que pode ser usado por um serviço de backdoor ou por um malware.  

pacote = IP(dst=host) / TCP(dport=portas, flags="S")
ans, unans = sr(pacote, inter=0.1, timeout=1)

print("PORTA\tESTADO")
for pacoteRecebido in ans:  # 1
    if pacoteRecebido[1].haslayer("ICMP"):  # 2
        if pacoteRecebido[1]["ICMP"].type == 3 and pacoteRecebido[1]["ICMP"].code == 3:  # 3
            print(pacoteRecebido[0][TCP].dport, "\tREJECT")  # 4
    elif pacoteRecebido[1].haslayer("TCP"):  # 5
        print(
            pacoteRecebido[1][TCP].sport,
            "\t",
            pacoteRecebido[1][TCP].sprintf("%flags%")
        )  # 6

for pacoteNaoRecebido in unans:  # 7
    print(pacoteNaoRecebido.dport, "\tDROP")
