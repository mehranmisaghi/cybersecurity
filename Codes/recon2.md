---
title: 'Teste de Invasão em Redes (I) - Reconhecimento (II)'
description: 'Testes de Reconhecimento - Alguns exemplos'
permalink: Codes/recon.md
---
>  os códigos apresentados nestas partes são baseados no livro **Python para Pentest (Daniel Moreno) Alguns códigos foram modificados por mim**. 
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