---
title: 'Teste de Invasão em Redes (I) - Reconhecimento'
description: 'Descoberta de DNS e algumas ferramentas'
permalink: Codes/recon.md
---

# 🔐 Alguns exemplos de teste de reconhecimento 

>  os códigos apresentados nestas partes são baseados no livro **Python para Pentest (Daniel Moreno) Alguns códigos foram modificados por mim**. 
---
⚠️ É importante enfatizar que qualquer tipo de teste em ambiente real precisa de consentimento da empresa, na qual serão realizados os testes.
---
# 💥 O que é um Reconhecimento na Rede faz mesmo?

Entender o ambiente antes de qualquer tentativa de exploração.

## 🔎 Atividades que poderão ser realizadas
- Coleta de informações públicas (OSINT)
- Identificação de:
  - Endereços IP
  - Domínios e subdomínios
  - Registros DNS
  - Tecnologias utilizadas
  - Estrutura da rede

---

# Descoberta de DNS

Neste primeiro exemplo, vamos tentar descobrir servidores de domínio, conforme o código *recon-dns.py*:
```python
import socket
dominio = "dominio.com"
nomes = ["ns1", "ns2", "www", "ftp", "intranet"]
for nome in nomes:
        DNS = nome + "." + dominio
        try:
            print (DNS + ":" + socket.gethostbyname(DNS))
        except socket.gaierror:
            pass
```
## 🔥 o que este programa vai trazer para mim?
vamos executar para ver.
- [Primeiro programa de descoberta de DNS](recon-dns.py)
---

# Vamos tentar descobrir mais informações?
No segundo exemplo, vamos tentar trazer as informações de forma mais específica, conforme o código *recon-dns-enum.py*:
```python
import dns.resolver
import dns.exception

dominio = "dominio.com"
registros = ["A", "AAAA", "MX", "NS"]

for registro in registros:
    try:
        resposta = dns.resolver.resolve(dominio, registro)

        for rdata in resposta:
            print(f"{registro}: {rdata}")

    except dns.resolver.NoAnswer:
        print(f"Sem resposta para o registro {registro}")
    except dns.resolver.NXDOMAIN:
        print(f"Domínio inexistente: {dominio}")
        break
    except dns.exception.Timeout:
        print("Timeout na consulta DNS")
    except dns.resolver.NoNameservers:
        print("Nenhum servidor DNS disponível")
```
## 🔥 o que este programa vai trazer para mim?
vamos executar para ver as informações
- [Segundo programa de descoberta de DNS](recon-dns-enum.py)

---
## ✅ Vamos conhecer as partes deste programa
 Você precisa inicialmente ter a biblioteca *dnspython*. Se não tiver, instale:
 ```
pip3 install dnspython
```
Lembrando que existem alguns tipos de registros de DNS:
## Tipos de Registros DNS

| Tipo  | Função                                   |
|-------|--------------------------------------------|
| A     | Retorna o endereço IP IPv4 do domínio      |
| AAAA  | Retorna o endereço IP IPv6 do domínio      |
| MX    | Indica o servidor de e-mail do domínio     |
| NS    | Indica os servidores DNS autoritativos do domínio |
---

## 🔥 Que outros programas posso usar além disso?

- nslookup
- dig
- Nmap
---

#  nslookup
```
nslookup dominio.com
```
```python
nslookup -type=MX dominio.com
nslookup -type=NS dominio.com
nslookup -type=AAAA dominio.com
```
---
# dig
```js
dig dominio.com A
dig dominio.com MX
dig dominio.com NS
dig dominio.com AAAA
```
---
#  Vamos testar e refletir sobre algumas questões

- Teste os dois programas em domínios diversos (precisa consentimento da empresa).
- Teste nslookup e dig nos mesmos domínios que você testes os dois programas. 
- Quais são diferenças nos testes (programa em python e app pronto como dig?)
- Os testes com dig e nslookup rodam em TCP ou UDP?
- Quais diferenças existem entre _Dig_ e _Nslookup_?

---
## O que vamos aprender agora?
[Transferência de Zona e WHOIS](recon2.md)

