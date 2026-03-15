--- 
title: 'Ameaças, Vulnerabilidades e Ataques'
description: 'Diversos tipos de ameaças, vulnerabilidades e ataques'
permalink: Intro/ameacas.md
---

# Aula 5.2 - Ameaças, Vulnerabilidades e Ataques


### **O que é uma ameaça?**
Ameaça normalmente consiste em uma situação, ação ou agente que pode explorar uma _vulnerabilidade_ e causar **dano à informação ou ao sistema**.

### **O que é uma vulnerabilidade?**
Vulnerabilidade consiste em _falha em sistemas, softwares, pessoas ou processos_ que pode ser explorada, resultando em riscos para a organização.

---

## 2. Principais Ameaças em Cibersegurança

- **Malware:** Softwares maliciosos como visto em [aula de malware](virus.md)
- **Engenharia Social:** Engano/manipulação para obter as informações por meio de persuação ou intimidação.
- **Ameaça Interna:** acesso indevido por usuários internos.

---

## 3. Algumas vulnerabilidades mais comuns

- Senhas fracas ou não trocadas
- Sistemas e softwares desatualizados/obsoletos/legados
- Configurações incorretas/expostas
- Falta de criptografia
- Dados sensíveis vazados ou publicamente acessíveis

**Referências:**
- [CVE – Common Vulnerabilities and Exposures](https://cve.mitre.org/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

## 4. Alguns tipos de Ataques Cibernéticos

### 4.1 Man-in-the-Middle (MITM)

Interceptação e possível alteração de comunicação entre duas partes sem que elas saibam.

---

### 4.2 Phishing

**Exemplo de e-mail phishing:**
```
De: suporte@dominiomalicioso.com
Assunto: Atualize Sua Senha

Prezado usuário,  
Sua conta foi comprometida. Clique [AQUI](http://sistemamalicioso.com) para redefinir sua senha.
```

---

### 4.3 SQL Injection
Explorar as vulenrabilidade de uma base de dados por meio de comoandos de sql.

### 4.4 Ataques de Força Bruta
Utilizar formas probailísticas de tentar a senha/token/pin (fatorial)

### 4.5 DDoS
Utilizar ferraemntas como ping distriubido para derrubar serviços/servidores. (usando ping) 
---

## 5. Como se proteger?

- Mantenha sistemas/softwares sempre atualizados.
- Use autenticação em dois ou mais fatores (2FA/MFA).
- Não reutilize senhas; crie senhas fortes.
- Oriente e treine usuários para identificar ataques.
- Faça backups regulares e teste sempre os seus backups.
- Revise permissões e minimize exposição de serviços.
- Faça monitoramento e auditoria constante.

---

## Referências

- [Cartilha de Segurança da Internet do NIC.br](https://cartilha.cert.br/)
- [OWASP Top 10 Project](https://owasp.org/www-project-top-ten/)
- [CVE Details](https://www.cvedetails.com/)
- [National Vulnerability Database do NIST](https://nvd.nist.gov/)

---
## O que vamos aprender agora?
- [Normas e frameworks de Segurança da Informação](/Frameworks/27000.md)
