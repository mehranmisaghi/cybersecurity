---
title: 'Teste de Invasão em Redes (I) - Reconhecimento (IV)'
description: 'Firewall e Banner'
permalink: Codes/recon4.md
---
>  os códigos apresentados nestas partes são baseados no livro **Python para Pentest (Daniel Moreno). Alguns códigos foram modificados por mim**. 
---
⚠️ É importante enfatizar que qualquer tipo de teste em ambiente real precisa de consentimento da empresa, na qual serão realizados os testes.
---
# 🔎 Firewall
Serve para descobrir o estado das portas. Vamos examinar o programa _recon-firewall.py_:

```python
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
```

## Vamos tentar entender um pouco do programa:

| Estado           | Significado                 |
|-----------------|--------------------------|
| SA        | Aberta|
| R ou RA      | Fechada             |
| nada    | Filtrada 🔒                    |
| ICMP unreachable       | rejeitada 🚫                       |

---
## Teste você mesmo este programa
- [Portas abertas](recon-firewall.py)
- Qual seria outra forma de fazer isto?
---
## Acesso Remoto

⚠️ Umas das preocupações com qualquer dispositivo deve ser o **Acesso Remoto**. Vamos examinar isto por meio do programa _recon-banner.py_:

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

try:
    sock.connect(("localhost", 22))
    data = sock.recv(2048)
    print(data.decode(errors="ignore"))
except Exception as e:
    print("Erro:", e)
finally:
    sock.close()
```
## Um programa simples, mas podoreso

- Se funcionar, traz a versão do programa de acesso remoto
- O que fazer para não funcionar?

## A nossa próxima aula

- [Criptografia]()