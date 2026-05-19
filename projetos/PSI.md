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
## Artefatos esperados do PSI

1. Descrição do sistema
2. Diagramas utilizados
    - classe
    - caso
    - UML
3. Dashboard de conformidade
    - % geral de conformidade
    - % por tipo de controle
    - gráficos (pizza ou barra)
4. Funcionalidade de comparativo
    - comparar com as auditorias anteriores
    - mostrar evolução de conformidade
5. Relatórios
    - parcial (por tipo de controle)
    - completo
    - opções:
        - comparativos
        - atual
---
## Fluxograma para PSI (sugestão)
> Diagrama propositalmente não acentuado
```mermaid
flowchart TD

    A[Inicio] --> B[Selecionar Modulo]

    B --> C{Modulo}

    C -->|27001| D[Carregar Controles SI]
    C -->|27701| E[Carregar Controles PI]

    D --> F[Informar nome da empresa]
    E --> F

    F --> G[Informar Data de Auditoria]

    G --> H[Iniciar Auditoria]

    H --> I[Exibir Controles]

    I --> J{Status}

    J -->|Conforme| K[Registrar Conforme]
    J -->|Nao Conforme| L[Perguntar andamento]
    J -->|Nao Aplica| M[Registrar Nao Aplica]

    L --> N{Existe andamento}

    N -->|Sim| O[Registrar Em Andamento]
    N -->|Nao| P[Registrar Nao Conforme]

    K --> Q{Mais controles}
    M --> Q
    O --> Q
    P --> Q

    Q -->|Sim| I
    Q -->|Nao| R[Finalizar Diagnostico]

    R --> S[Armazenar Dados]

    S --> T[Gerar Dashboard]

    T --> U[Calcular Conformidade]
    T --> V[Agrupar Controles]
    T --> W[Gerar Graficos]

    U --> X[Exibir Dashboard]
    V --> X
    W --> X

    X --> Y{Gerar relatorio}

    Y -->|Sim| Z{Relatorio comparativo?}
    Y -->|Nao| AF[Fim]

    Z -->|Sim| AA{Tipo}
    Z -->|Nao| AB{Tipo}

    AA -->|Parcial| AC[Relatorio Parcial Comparativo]
    AA -->|Completo| AD[Relatorio Completo Comparativo]

    AB -->|Parcial| AE[Relatorio Parcial Atual]
    AB -->|Completo| AG[Relatorio Completo Atual]

    AC --> AF
    AD --> AF
    AE --> AF
    AG --> AF
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
