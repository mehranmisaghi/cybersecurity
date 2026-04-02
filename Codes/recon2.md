---
title: 'Teste de Invasão em Redes (I) - Reconhecimento (II)'
description: 'Testes de Reconhecimento - Alguns exemplos'
permalink: Codes/recon2.md
---
>  os códigos apresentados nestas partes são baseados no livro **Python para Pentest (Daniel Moreno). Alguns códigos foram modificados por mim**. 
---
⚠️ É importante enfatizar que qualquer tipo de teste em ambiente real precisa de consentimento da empresa, na qual serão realizados os testes.
---

# 🔥 Transferência de Zona de DNS 
Neste exemplo vamos tentar verificar a possiblidade de transferência de Zona de DNS (vamos explicar para que serve isto)

## O que é uma Transferência de zona?
Por default, os servidores DNS podem fazer transferência de zona entre si para sincronização de conteúdo, por exemplo um servidor primário para outro servidor (secundário). Se algum servidor estiver configurado de forma incorreta, permitirá a transferência para *qualquer endereço IP*. 

🔥 Se isto for possível, você pode copiar **todos os registros do domínio!**
---
Agora vamos ver um código que tenta fazer a trasferência da zona, aqui denominado por *recon-dns-transfer.py*:

```python
import dns.query
import dns.zone
import dns.resolver

dominio = "dominio.com"

registrosNS = dns.resolver.resolve(dominio, "NS")

lista = []

for registro in registrosNS:
    lista.append(str(registro).rstrip("."))

for registro in lista:
    try:
        print(f"Tentando transferência de zona em {registro}...")

        transferenciaZona = dns.zone.from_xfr(
            dns.query.xfr(registro, dominio)
        )

    except Exception as e:
        print(f"Erro na transferência de zona: {e}")

    else:
        registroDNS = sorted(transferenciaZona.nodes.keys())

        for n in registroDNS:
            print(transferenciaZona[n].to_text(n))
```
## 🎯 Se a transferência funcionar, você poderá ter as seguintes informações:

- www.dominio.com
- mail.dominio.com
- ftp.dominio.com
- dev.dominio.com
- intranet.dominio.com
- registros MX
- registros TXT
- registros internos

Quer dizer, **um mapa completo da infraestrutura DNS**. Espero que não funcione!
---
## Teste você mesmo este programa
[Programa de Transferência de Zona DNS](recon-dns-transfer.py)
- Teste o programa com domínios conhecidos (com consentimento).
- Quais são ações que parecisam ser feitas caso o programa trazer as informações completas?

# 🔎 WHOIS
WHOIS pode ser definido como um serviço que traz informações a respeito do registo de um domínio:

- 📅 Data de criação
- 📅 Data de expiração
- 🏢 Organização responsável
- 📧 Email de contato
- 🌐 Servidores DNS
- 🔒 Status do domínio

---
Agora vamos ver um código que tenta busdar as informações do registro de domínio, aqui denominado por *recon-whois.py* :
Você precisa inicialmente ter a biblioteca *python-whois*. Se não tiver, instale:
 ```
pip3 install python-whois
```
```python

import whois 

dominio = "dominio.com"

try:
    consultaWhois = whois.whois(dominio)

    print("Email (atributo):", consultaWhois.email)
    print("Email (chave):", consultaWhois.get("email"))
    print("Texto completo:\n", consultaWhois.text)

except Exception as e:
    print("Erro ao consultar WHOIS:", e)   
```
---
## Teste você mesmo este programa
[Busca de informações de registro](recon-whois.py)
- Qual seria outra forma de fazer isto?
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
-[Ping Sweep](recon-ping.py)

## Se não funcionar?
- Tem que executar como _root_ 
- Bloqueio por parte de firewall para requisições ICMP
- Um site ativo também pode ter bloqueio para requisições ICMP




