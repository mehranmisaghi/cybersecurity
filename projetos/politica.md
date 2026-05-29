---
title: 'PSI e PPI'
description: 'Política de Segurança da Informação e Política de Privacidade da Informação'
permalink: politica.md
---

#  Política de Segurança da Informação e Política de Privacidade da Informação

---

## O que é Política de Segurança da Informação?

A Política de Segurança da Informação pode ser definido como um conjunto de procedimentos que definem como uma organização protege seus ativos de informação. Esta política tem por objetivo assegurar confidencialidade, integridade e disponibilidade.

### Exemplos de Políticas de Segurança da Informação:
- Controle de acesso
- Uso de senhas
- Backup de dados
- Uso de redes sociais

---

## O que é Política de Privacidade da Informação

A Política de Privacidade define como os dados pessoais são (tendo em foco a proteção de dados pessoais, transparência e direitos do titular):

- Coletados
- Utilizados
- Armazenados
- Compartilhados
- Protegidos

---

## Gestão de Riscos
Risco é a possibilidade de um evento causar impacto negativo à organização. [Para melhor entendimento veja novamente os conceitos de riscos](griscos.md)

---

## Etapas de Elaboração de Políticas

```mermaid
flowchart 
A[Contexto] --> B[Ativos]
B --> C[Riscos]
C --> D[Controles]
D --> E[Politica]
E --> F[Implementacao]
F --> G[Monitoramento]
G --> H[Revisao]
```
## Etapas detalhadas
```mermaid
flowchart TD

A[Entender Contexto] --> B[Identificar Ativos]
B --> C[Analisar Riscos]

C --> D[Definir Controles]

D --> E[Elaborar Politica]

E --> F[Implementar]
F --> G[Monitorar]

G --> H[Revisar e Melhorar]


A --> A1[Tipo de organizacao]
A --> A2[Regulamentacoes]

B --> B1[Dados]
B --> B2[Sistemas]
B --> B3[Pessoas]

C --> C1[Ameacas]
C --> C2[Vulnerabilidades]
C --> C3[Impacto]

D --> D1[Controle de acesso]
D --> D2[Criptografia]
D --> D3[Backup]

E --> E1[Objetivo]
E --> E2[Escopo]
E --> E3[Regras]

F --> F1[Treinamento]
F --> F2[Divulgacao]

G --> G1[Auditoria]
G --> G2[Logs]

H --> H1[Melhoria continua]
```
---
## [Projeto de Segurança II](PSII.md)