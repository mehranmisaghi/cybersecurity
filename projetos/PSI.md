# Projeto de Segurança I (PSI) 12 a 25 de maio
Com os conceitos apreendidos os alunos **(em até 3 pessoas)** precisam desenvolver uma ferramenta que auxilie no diagnóstico da conoformidade (conforme, não conforme ou não aplica). As apresentações poderão ser feitas até dia **25/05**. Escolham cenários reais para aplicação.
- _O que o seu sistema deve ter?_
    - Um módulo para 27001 e outro para 27701.
    - Utilizar 27002 para diagnóstico da conformidade de 27001.
    - Perguntar none da data e data de auditoria.
    - Para cada controle, perguntar se está conforme ou não está conforme ou não se aplica. Caso não esteja conforme, perguntar se existe alguma trabalho em andamento.
    - Apresentar os dados no formato de dashboard:
      - Agrupar os dados por tipos de controle (27002)
      - Apresentar gráficos de conformidade agrupado por tipos de controles (parciais) e total.
    - Armazenar os dados e data de diagnóstico para efeitos comparativos.
    - Fazer UML da ferramenta.
    - Apresentar relatórios por tipos de controle ou relatório completo de conformidade.
--- 
## Fluxograma para PSI (sugestão)

```mermaid
flowchart TD

    A[Início] --> B[Selecionar Módulo]

    B --> C{Qual módulo?}

    C -->|ISO 27001| D[Carregar Controles via ISO 27002]
    C -->|ISO 27701| E[Carregar Controles de Privacidade]

    D --> F[Informar Nome da Empresa]
    E --> F

    F --> G[Informar Data da Auditoria]

    G --> H[Iniciar Diagnóstico]

    H --> I[Exibir Controle]

    I --> J{Status do Controle?}

    J -->|Conforme| K[Registrar como Conforme]
    J -->|Não Conforme| L[Perguntar se há trabalho em andamento]
    J -->|Não se aplica| M[Registrar como Não Aplicável]

    L --> N{Existe trabalho em andamento?}

    N -->|Sim| O[Registrar como Em Andamento]
    N -->|Não| P[Registrar como Não Conforme]

    K --> Q{Há mais controles?}
    M --> Q
    O --> Q
    P --> Q

    Q -->|Sim| I
    Q -->|Não| R[Finalizar Diagnóstico]

    R --> S[Armazenar Dados + Data]

    S --> T[Gerar Dashboard]

    T --> U[Calcular % Conformidade Geral]
    T --> V[Agrupar por Tipo de Controle (ISO 27002)]
    T --> W[Gerar Gráficos (Pizza/Barra)]

    U --> X[Exibir Dashboard]
    V --> X
    W --> X

    X --> Y{Deseja relatório?}

    Y -->|Sim| Z[Gerar Relatório]
    Y -->|Não| AA[Fim]

    Z --> AB{Tipo de Relatório}

    AB -->|Por tipo de controle| AC[Relatório Parcial]
    AB -->|Completo| AD[Relatório Geral]

    AC --> AA
    AD --> AA
    ```
---

## Grupos de Trabalho(18/05)
1. Maria Fernanda e Pedro
2. Ricardo, Paulo e Gabriel Gomes
3. João, Stephine e Alexssandro
4. Sidnei, Luiz e Gabriel Lopes
5. Otavio, José e Fábio
6. Camila, Gabriela e Sidiclei
---
