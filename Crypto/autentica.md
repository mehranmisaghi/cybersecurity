# 🔐 Autenticação e Kerberos 
  
![Security](https://img.shields.io/badge/Security-Authentication-blue)
![Criptografia](https://img.shields.io/badge/Cryptography-Symmetric%20%26%20Asymmetric-green)
![Kerberos](https://img.shields.io/badge/Protocol-Kerberos-orange)
![Status](https://img.shields.io/badge/Status-Study%20Notes-success)

> 📘 Resumo gerado com auxílio de IA do capítulo 15 (autenticação) e revisado.
- [Capítulo 15 do livro Stallings](https://mehranmisaghi.github.io/cybersecurity/materiais/cap15-stallings.pdf)

---

## 🔐 Conceitos Fundamentais

### 🧩 Etapas da Autenticação

```mermaid
flowchart LR
A[Usuário] --> B[Identificação]
B --> C[Verificação]
C --> D[Acesso Permitido]
```

---

### 🔑 Fatores de Autenticação

| Tipo | Exemplo |
|------|--------|
| 🧠 Algo que tem conhecimento | Senha, PIN |
| 📱 Dispositivo | Token, Cartão |
| 👤 Característica física | Biometria |
| ⌨️ Padrão de comportamento | Padrão de digitação |

---

## 🔄 Autenticação Mútua & Segurança

### 🤝 Autenticação Mútua

```mermaid
sequenceDiagram
participant A as Cliente
participant B as Servidor

A->>B: Solicita autenticação
B->>A: Desafio
A->>B: Resposta
B->>A: Confirmação
```

---

### ⚠️ Principais Ataques

- 🔁 Replay Attack (repetição)
- 🎭 Personificação
- 📡 Interceptação

### 🛡️ Proteções

- Timestamp ⏱️  
- Nonce 🔢  
- Desafio-resposta 🔐  

---

## 🔑 Criptografia Simétrica

```mermaid
flowchart TD
A[Cliente] -->|Chave secreta| B[KDC]
B -->|Gera chave de sessão| A
B -->|Gera chave de sessão| C[Servidor]
A --> C
```

### ✔️ Características:
- Uso de chave compartilhada
- Alto desempenho

### ❌ Desvantagens:
- Distribuição de chaves complexa
- Vulnerável a replay

---

## 📧 Autenticação em Sistemas Assíncronos

- Comunicação não simultânea (ex: e-mail)
- Uso de criptografia para garantir:
  - Confidencialidade
  - Autenticidade

---

## 🛡️ Kerberos

### 📌 Visão Geral

Sistema de autenticação centralizado baseado em criptografia simétrica.

---

### 🧠 Arquitetura

```mermaid
flowchart LR
User[Usuário] --> AS[Authentication Server]
AS --> TGS[Ticket Granting Server]
TGS --> Service[Servidor de Serviço]
```

---

### 🔄 Funcionamento

```mermaid
sequenceDiagram
participant U as Usuário
participant AS as Auth Server
participant TGS as Ticket Server
participant S as Serviço

U->>AS: Login
AS->>U: Ticket TGS
U->>TGS: Solicita serviço
TGS->>U: Ticket Serviço
U->>S: Acessa serviço
```

---

### ✅ Vantagens

- 🔐 Senhas não trafegam na rede
- 🔁 Single Sign-On (SSO)
- 🏢 Centralização da autenticação

### ❌ Limitações

- Dependência do servidor Kerberos
- Sincronização de tempo necessária

---

## 🔐 Criptografia Assimétrica

```mermaid
flowchart LR
A[Chave Pública] --> B[Criptografia]
B --> C[Dados]
C --> D[Descriptografia]
D --> E[Chave Privada]
```

### ✔️ Benefícios:
- Segurança elevada
- Não requer compartilhamento prévio de chave

---

## 🌐 Identidade Federada

> 🔗 Um único login para múltiplos sistemas

### Exemplos:
- Google
- Facebook
- Microsoft

### ✔️ Vantagens:
- Melhor experiência do usuário
- Menos senhas

---

## 🧾 PKI (Infraestrutura de Chaves Públicas)

```mermaid
flowchart TD
CA[Autoridade Certificadora] --> Cert[Certificado Digital]
Cert --> User[Usuário]
User --> Verify[Verificação de Identidade]
```

### Componentes:
- Certificados digitais
- Assinaturas digitais
- Autoridades certificadoras
---
##  [Slides da Aula - Criptografia (III)](https://canva.link/3imxx00leivyomj)


## [Voltar para Criptografia](README.md)