---
title: 'Classificação das informações'
description: 'Fundamenetos de classificação da informação'
permalink: Intro/classificacao.md
---
   
# Classificação da Informação

A ideia deste documento é auxiliar de forma bastante prática compreender a necessidade e forma de **classificar a informação**. pois:

- Conforme a NBR ISO/IEC 27002:2022: "Convém que as informações sejam classificadas de acordo com as necessidades de segurança da informação da organização com base na confidencialidade, integridade, disponibilidade e requisitos relevantes das partes interessadas". 

Mas, onde se aplica a classificação?

 - A classificação deve ser aplicada a qualquer informação produzida, recebida ou mantida pelo time (documentos, planilhas, e-mails, tickets, logs, dumps, backups, prints, repositórios, anexos, etc.).

---

## Quais são os objetivos de classificação?

- Reduzir risco de vazamento e uso indevido de informação
- Padronizar como dados são rotulados e manuseados
- Ajudar na conformidade com requisitos legais (LGPD, por exemplo)
- Definir controles mínimos de segurança por tipo de informação (_Falamos sobre isto na última aula_)

---

## Como fazer isto?

- **Menor privilégio**: acesso apenas para quem precisa.
- **Necessidade de saber**: mesmo com acesso ao sistema, nem tudo deve ser visível.
- **Classificação pelo conteúdo** (não pelo formato): uma foto pode ser mais sensível que um PDF.
- **Na dúvida, classifique com menor privilégio**
- **Revisão periódica**: a classificação pode mudar com o tempo.

---

## Níveis de classificação (modelo recomendado)

| Nível | Descrição | Exemplos | Regra de compartilhamento |
|------|-----------|----------|---------------------------|
| Público | Informação que pode ser de conhecimento de qualquer pessoa sem impacto relevante se **exposta**. | material da minha aula, posts de marketing, documentação aberta. | Pode ser compartilhada com qualquer pessoa |
| Interno | Informação para uso dentro do time/empresa. Exposição gera baixo a moderado impacto. | Roadmap interno, atas, decisões internas.| Somente pessoas autorizadas internas. |
| Confidencial | Informação sensível de negócio/cliente/operação. Exposição pode causar dano relevante. | Dados de clientes, contratos, tabelas de preços não públicos, credenciais, controle de incidentes. | Acesso restrito  |
| Restrito (ou Secreto) | Informação crítica. Exposição pode causar dano irreparável (financeiro, reputacional) ou comprometer segurança. | senhas, chaves privadas, dados pessoais sensíveis, dumps de equipamentos.| Acesso altamente restrito, controles fortes. |


---

## Como classificar (passo a passo)

1. **Identifique o tipo de dado**
   - Dados pessoais? Dados de cliente? Estratégia de negócio?
2. **Avalie o impacto se vazar**
   - Baixo, moderado, alto, severo(muito alto)
3. **O que não pode ser esquecido**
   - LGPD, contratos, NDAs, políticas internas, requisitos de auditoria de uma determinada norma.
4. **Escolha o nível mais restritivo aplicável**
5. **Rotule e aplique controles**
   - Toda informação, segundo a norma NBR ISO/IEC 27002:2022, precisa ter rótulo.

---
## Exemplos rápidos

- Descrição técnica do produto: **Interno**
- Lista de clientes com e-mails: **Confidencial**
- Tags com token de apps: **Restrito**
- Missão e visão da empresa: **Público**
- Logs de eventos de autenticação: **Confidencial** 

---
## Bora exercitar agora!

Veja a necessidade de cada situação e classifique as informações
---

## Cenário 1 — Documentação de projeto
Seu time quer publicar no GitHub uma página com a visão geral da arquitetura do sistema, incluindo:
- nomes de serviços e responsabilidades
- exemplos de carga de trabalho (sem dados reais)
- nomes de times e ferramentas (dev/hml/prod)
---

## Cenário 2 — Planilha com dados de clientes
Uma analista compartilha por e-mail uma planilha contendo:
- nome completo
- e-mail
- telefone
- data de nascimento
- status de pagamento
- observações de atendimento
---

## Cenário 3 — Credenciais e tokens
Durante um incidente, alguém cola no chat do time:
- um token de acesso (ainda válido) para uma API interna
- um trecho de configuração contendo URL do serviço 
- instruções rápidas para “testar” a chamada
---

## Cenário 4 — Resultados financeiros e estratégia
Você vai apresentar em uma reunião um documento com:
- receita mensal detalhada por produto
- previsão de faturamento do próximo trimestre
- custos por fornecedor
- percentuais de reajuste de preços
---

