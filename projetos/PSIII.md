# Projeto de Segurança III: Automação de Diagnóstico de Vulnerabilidades com IA

---

## Objetivo

Desenvolver uma ferramenta automatizada utilizando agentes de IA (como n8n ou similares) capaz de realizar diagnóstico de vulnerabilidades, identificando riscos e sugerindo ações corretivas.

---

## Descrição

A solução deve:

- Coletar informações do sistema alvo  
- Identificar vulnerabilidades  
- Classificar riscos  
- Sugerir medidas de mitigação  

A ferramenta deve operar de forma automatizada, simulando um processo de auditoria de segurança.

---

## Cenários Disponíveis

Escolher **um dos cenários abaixo**:

---

### Cenário 1 – Servidor Web

A ferramenta deve:

- Analisar protocolos criptográficos (SSL/TLS)  
- Identificar configurações inseguras  
- Avaliar certificados digitais  
- Detectar falhas de configuração  

#### Saídas esperadas:
- Lista de vulnerabilidades  
- Classificação de risco  
- Recomendações de correção  
```mermaid
flowchart TD

A[Definir alvo servidor web] --> B[Coletar informacoes]

B --> C[Verificar protocolos SSL TLS]
C --> D{Protocolo seguro}

D -->|Nao| E[Identificar vulnerabilidade criptografica]
D -->|Sim| F[Validar configuracao]

F --> G[Analisar certificado digital]
G --> H{Certificado valido}

H -->|Nao| I[Identificar falha de certificado]
H -->|Sim| J[Continuar analise]

E --> K[Classificar risco]
I --> K

J --> L[Verificar configuracoes gerais]
L --> M[Identificar falhas de configuracao]

M --> N[Classificar risco]
K --> N

N --> O[Gerar recomendacoes]
O --> P[Gerar relatorio final]
```
---

### Cenário 2 – Banco de Dados via Web

A ferramenta deve:

- Identificar vulnerabilidades de SQL Injection  
- Simular entradas maliciosas  
- Detectar falhas de validação  
- Avaliar exposição de dados  

#### Saídas esperadas:
- Pontos vulneráveis  
- Classificação de risco  
- Recomendações de mitigação  

---

## Requisitos Técnicos

- Utilizar ferramenta de automação (ex: n8n)  
- Integrar fluxo de coleta, análise e resposta  
- Implementar lógica automatizada  
- Gerar saída em relatório ou dashboard  

---

## Requisitos de Segurança

- Seguir boas práticas de segurança  
- Não executar testes destrutivos  
- Utilizar ambiente controlado  
```mermaid
flowchart TD

A[Definir aplicacao alvo] --> B[Coletar entradas de usuario]

B --> C[Simular entradas maliciosas]
C --> D[Testar SQL Injection]

D --> E{Sistema vulneravel}

E -->|Sim| F[Identificar ponto vulneravel]
E -->|Nao| G[Validar seguranca]

F --> H[Analisar impacto]
H --> I[Classificar risco]

G --> J[Continuar verificacoes]
J --> K[Analisar validacao de entrada]

K --> L{Validacao adequada}

L -->|Nao| F
L -->|Sim| M[Sem vulnerabilidade critica]

I --> N[Gerar recomendacoes]
M --> N

N --> O[Gerar relatorio final]
```
---

## Artefatos esperados

### Documentção
- Objetivo  
- Arquitetura  
- Tecnologias  

### Fluxo
- Diagrama do processo  

### Sistema
- Protótipo funcional  

### Relatório
- Vulnerabilidades  
- Riscos  
- Recomendações  

---

## Fluxo sugerido da solução

```mermaid
flowchart TD
A[Entrada do alvo] --> B[Coleta de dados]
B --> C[Analise automatizada]
C --> D[Identificacao de vulnerabilidades]
D --> E[Classificacao de risco]
E --> F[Geracao de recomendacoes]
F --> G[Relatorio ou Dashboard]
```