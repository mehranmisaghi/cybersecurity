---
title: 'Teste de Invasão em Redes (I) - Reconhecimento (III)'
description: 'Port Scanner, Ping Sweep e Arping'
permalink: Codes/recon3.md
---
>  os códigos apresentados nestas partes são baseados no livro **Python para Pentest (Daniel Moreno). Alguns códigos foram modificados por mim**. 
---
⚠️ É importante enfatizar que qualquer tipo de teste em ambiente real precisa de consentimento da empresa, na qual serão realizados os testes.
---
# 🔎 Port Scanner
Serve para descobrir portas abertas em um determando IP. Pode ser feito em IPv4 ou IPv6. Vamos ver cada um deles. Antes disso, precisamo instalar a biblioteca *scapy*
```
pip3 install scapy
``` 

## Port Sanner IPv4

```python
from scapy.all import * # versão de programa IPv4 

conf.verb = 0  # Desativa mensagens detalhadas do Scapy

portas = [21, 22, 23, 80, 8080]

# Substitua pelo IP real de destino
pacoteIP = IP(dst="142.250.78.110") #endereço de google.com apenas como exemplo

pacoteTCP = TCP(dport=portas, flags="S")
pacote = pacoteIP / pacoteTCP

ans, unans = sr(pacote, inter=0.1, timeout=1)

print("Porta\tEstado")

for pacoteEnviado, pacoteRecebido in ans:
    porta = pacoteRecebido[TCP].sport
    flags = pacoteRecebido[TCP].sprintf("%flags%")
    print(f"{porta}\t{flags}")
```
## Vamos tentar entender um pouco algumas portas

| Porta           | Serviço                  |
|-----------------|--------------------------|
| 21        | FTP|
| 22       | SSH             |
| 23    | Telnet                         |
| 80           | HTTP                           |
| 8080        | HTTP alternativo                             |
---
## Como deveria ser a resposta do programa?
| Flag          | Significado              |
|-----------------|--------------------------|
| SA        | SYN-ACK (porta aberta)|
| R     |Reset (Porta fechada)             |
---
## Se não tiver resposta? (normalmente pode ser:)
- Bloqueio por firewall
- execução sem permissão de root
---
## Teste você mesmo este programa
[Port scanner IPv4](recon-portscanner4.py)
- Qual seria outra forma de fazer isto?
---
## Port Sanner IPv6

- Antes de executar programa com IPv6, precisa saber se sua rede opera no IPv6. Para isto, execute o seguinte comando (linux/mac)
```
ping6 www.google.com
```
No caso de windows:
```
ping -6 www.google.com
```
Se responder, é sinal que a sua rede opera ativamente IPv6.

```python
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
```
## Se não tiver resposta? (normalmente pode ser:)
- A maioria dos servidores bloqueiam IPv6 
- Bloqueio por firewall
- execução sem permissão de root

## Ping Sweep

> Esta técnica que faz parte de reconhecimento **(RECON)**, manda ping para cada IP de uma faixa de IP e espera a resposta e apresenta os _hosts_ que responderam (ativos) e os que não responderam (inativos). Pode ser utilizado junto com a técnica de varredura de portas. Neste exemplo, **não faremos isto**. 
---
vamos ver um exemplo deste tipo de programa, no código de _recon-ping.py_, que utiliza a técnica de _ping sweep_:

```python
from scapy.all import IP, ICMP, sr, conf

conf.verb = 0

IPs = []

for ip in range(1, 255):
    IPs.append("192.168.0." + str(ip)) #substitua por faixa de IP da sua rede com autorização

pacote = IP(dst=IPs) / ICMP()
ans, unans = sr(pacote, inter=0.1, timeout=1)

print("Hosts ativos")

for enviado, recebido in ans:
    print(recebido[IP].src)

# Para determinar os hosts inativos:
print("Hosts inativos")
for pacoteNaoRecebido in unans:
    print(pacoteNaoRecebido[IP].dst)
```
## Vamos testar?
- [Ping Sweep](recon-ping.py)

## Se não funcionar?

- Tem que executar como _root_ 
- Bloqueio por parte de firewall para requisições ICMP
- Um site ativo também pode ter bloqueio para requisições ICMP

## Arping

> Esta técnica que faz parte de reconhecimento **(RECON)**, faz uma varredura para os dispositivos que estão ativos e seus _Mac address_. 
---
vamos ver um exemplo deste tipo de programa, no código de _recon-arping.py_:

```python
from scapy.all import Ether, ARP, srp, conf

conf.verb = 0

IPs = []

for ip in range(1, 255):
  IPs.append("10.1.0" + str(ip))
  #  IPs.append("teste com endereços da sua rede" + str(ip))

pacoteARP = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=IPs)
ans, unans = srp(pacoteARP, inter=0.1, timeout=1)

print("IP\t\tMAC")

for enviado, recebido in ans:
    print(f"{recebido.psrc}\t{recebido.hwsrc}")
```
## Quais diferenças com Ping Sweep?

Diferente do ping (ICMP):

- ✅ ARP não é bloqueado facilmente.

- ✅ ARP descobre _MAC Address_. (Isto é bom ou ruim?)

- ✅ Funciona melhor em redes locais. (Isto é bom ou ruim?)

- ✅ Detecta hosts mesmo com firewall.

- ❌ Não funciona na Internet.

## O que vamos aprender agora?
[Portas Abertas e Acesso Remoto](recon4.md)
