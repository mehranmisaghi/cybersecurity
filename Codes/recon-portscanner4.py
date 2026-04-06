from scapy.all import * # versão de programa IPv4 

conf.verb = 0  # Desativa mensagens detalhadas do Scapy

portas = [21, 22, 23, 80, 8080]

# Substitua pelo IP real de destino
pacoteIP = IP(dst="158.69.19.64") #endereço de google.com apenas como exemplo

pacoteTCP = TCP(dport=portas, flags="S")
pacote = pacoteIP / pacoteTCP

ans, unans = sr(pacote, inter=0.1, timeout=1)

print("Porta\tEstado")

for pacoteEnviado, pacoteRecebido in ans:
    porta = pacoteRecebido[TCP].sport
    flags = pacoteRecebido[TCP].sprintf("%flags%")
    print(f"{porta}\t{flags}")
