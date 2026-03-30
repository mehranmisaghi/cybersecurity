from scapy.all import IPv6, TCP, sr, conf

conf.verb = 0

portas = [80, 443]

#pacoteIP = IPv6(dst="2001:4860:4860::8888")  # Google DNS IPv6 como exemplo
pacoteIP = IPv6(dst="2800:3f0:4001:800::200e")  # Google DNS IPv6 como exemplo
pacoteTCP = TCP(dport=portas, flags="S")

pacote = pacoteIP / pacoteTCP

ans, unans = sr(pacote, timeout=2)

print("Porta\tEstado")

for enviado, recebido in ans:
    if recebido[TCP].flags == 0x12:
        print(f"{recebido[TCP].sport}\tAberta")
    elif recebido[TCP].flags == 0x14:
        print(f"{recebido[TCP].sport}\tFechada")
