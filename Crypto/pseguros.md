# 🛡️ Protocolos Seguros

> Material gerado com auxílio de IA e revisado.

---

## 📘 1. O que são Protocolos Seguros?

Protocolos seguros são conjuntos de regras de comunicação que usam recursos de **criptografia**, **autenticação** e **integridade** para proteger informações transmitidas em redes de computadores.

### Eles garantem:

- 🔒 **Confidencialidade** → impede que pessoas não autorizadas leiam os dados
- ✅ **Integridade** → assegura que a mensagem não foi alterada
- 👤 **Autenticação** → confirma a identidade das partes envolvidas

---

## 🌐 2. Principais Protocolos Seguros

### 🔒 HTTPS (HyperText Transfer Protocol Secure)

- **Uso principal:** navegação segura em sites
- **Base:** HTTP + TLS
- **Porta padrão:** `443`
- **Função:** proteger dados como senhas, pagamentos e informações pessoais
- **Importância atual:** é o padrão de segurança da web moderna

💡 Sempre que um site usa HTTPS, normalmente aparece um **cadeado** no navegador.

---

### 💻 SSH (Secure Shell)

- **Uso principal:** acesso remoto seguro a servidores
- **Substitui:** Telnet
- **Porta padrão:** `22`
- **Função:** permitir execução de comandos remotos com criptografia

💡 Muito usado por administradores de sistemas e desenvolvedores.

---

### 📁 SFTP (SSH File Transfer Protocol)

- **Uso principal:** transferência segura de arquivos
- **Base:** protocolo SSH
- **Porta padrão:** `22`
- **Função:** enviar e receber arquivos de forma protegida

⚠️ **Importante:** SFTP não é a mesma coisa que FTPS.

---

### 📧 SMTPS (Simple Mail Transfer Protocol Secure)

- **Uso principal:** envio seguro de e-mails
- **Base:** SMTP + TLS
- **Portas comuns:** `465` e `587`
- **Função:** criptografar o envio de mensagens entre cliente e servidor

💡 Muito utilizado em serviços como Gmail, Outlook e provedores corporativos.

---

## 🔐 3. Outros Protocolos Seguros Importantes

### 🔐 TLS 1.3 (Transport Layer Security)

- **Função:** base da segurança moderna da internet
- **Usado em:** HTTPS, SMTPS, FTPS e outros
- **Vantagem:** mais rápido e seguro que versões anteriores

---

### 🌐 IPsec

- **Uso principal:** criação de VPNs
- **Nível de atuação:** camada de rede
- **Função:** proteger todo o tráfego IP entre dispositivos

---

### 📁 FTPS (File Transfer Protocol Secure)

- **Uso principal:** transferência segura de arquivos
- **Base:** FTP + TLS
- **Diferença para SFTP:** FTPS usa TLS; SFTP usa SSH

---

### 🧭 DNSSEC (Domain Name System Security Extensions)

- **Uso principal:** proteger o sistema de nomes de domínio (DNS)
- **Função:** evitar falsificação de respostas DNS
- **Benefício:** ajuda a impedir redirecionamento para sites falsos

---

### 📶 WPA3

- **Uso principal:** segurança em redes Wi-Fi
- **Função:** proteger a comunicação entre dispositivos e roteadores
- **Vantagem:** segurança mais forte em comparação ao WPA2

---

## 📊 4. Resumo Comparativo

| Protocolo | Uso Principal | Base de Segurança | Porta Padrão |
|----------|---------------|------------------|-------------|
| HTTPS | Navegação web | TLS | 443 |
| SSH | Acesso remoto | Criptografia própria | 22 |
| SFTP | Transferência de arquivos | SSH | 22 |
| SMTPS | Envio de e-mail | TLS | 465 / 587 |
| FTPS | Transferência de arquivos | TLS | 990 / 21 |
| IPsec | VPN | Criptografia de comunicação | Variável |
| DNSSEC | Segurança DNS | Assinatura digital | — |
| WPA3 | Redes Wi-Fi | Criptografia melhorada | — |

---

## 🧠 5. Diferenças Importantes

### HTTPS x HTTP
- **HTTP:** envia dados sem proteção
- **HTTPS:** envia dados com criptografia usando TLS

### SSH x Telnet
- **Telnet:** envia tudo em texto puro
- **SSH:** protege a conexão com criptografia

### SFTP x FTPS
- **SFTP:** funciona com SSH
- **FTPS:** funciona com TLS

---


## 📚 7. Referências utilizada

**IETF.** *The Transport Layer Security (TLS) Protocol Version 1.3*. RFC 8446, 2018. Disponível em: https://datatracker.ietf.org/doc/html/rfc8446

**IETF.** *HTTP Over TLS*. RFC 2818, 2000. Disponível em: https://datatracker.ietf.org/doc/html/rfc2818

**IETF.** *The Secure Shell (SSH) Protocol Architecture*. RFC 4251, 2006. Disponível em: https://datatracker.ietf.org/doc/html/rfc4251

**IETF.** *SMTP Service Extension for Secure SMTP over Transport Layer Security*. RFC 3207, 2002. Disponível em: https://datatracker.ietf.org/doc/html/rfc3207

**IETF.** *DNS Security Introduction and Requirements*. RFC 4033, 2005. Disponível em: https://datatracker.ietf.org/doc/html/rfc4033

**IETF.** *Security Architecture for the Internet Protocol*. RFC 4301, 2005. Disponível em: https://datatracker.ietf.org/doc/html/rfc4301

**KUROSE, James F.; ROSS, Keith W.** *Computer Networking: A Top-Down Approach*. 8. ed. Pearson, 2021.

**STALLINGS, William.** *Network Security Essentials: Applications and Standards*. 7. ed. Pearson, 2020.

**TANENBAUM, Andrew S.; WETHERALL, David J.** *Computer Networks*. 6. ed. Pearson, 2021.

**NIST.** *Digital Signature Standard (DSS)*. FIPS PUB 186-5, 2023. Disponível em: https://csrc.nist.gov

---

### [Teste os seus conhecimentos sobre protocolos seguros](https://mehranmisaghi.github.io/cybersecurity/Crypto/pseguros3.html)
### [Voltar](README.md)
---

