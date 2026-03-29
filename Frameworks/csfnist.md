--- 
title: 'Alguns Frameworks selecionados'
description: 'NIST CSF, NIST 800-53 (r5) e FISMA'
permalink: Framewoks/csfnist.md
---

# Aula 7.3 - NIST Cybersecurity Framework (CSF), NIST SP 800-53 Rev. 5 e FISMA

---

## NIST Cybersecurity Framework (CSF)

O NIST CSF é um framework amplamente adotado para gerenciar os riscos envovlidos em  cibersegurança, focando e facilitando:
- alinhamento com objetivos de negócio,
- priorização de investimentos,
- comunicação entre áreas técnicas e executivas,
- melhoria contínua (nem sempre isto é possível)

[Referência utilizada](https://www.nist.gov/cyberframework)


###  Estrutura do CSF (CSF 2.0)
O CSF organiza práticas e resultados em níveis que facilitam planejamenton por área de atuação:

- **Funções**: áreas macro (ex.: Govern, Identify, Protect, Detect, Respond, Recover).
- **Categorias e Subcategorias**: Resultados mais específicos.
- **Perfis**:
  - Perfil Atual: o que já existe e seu nível de atendimento.
  - Perfil pretendido: o que deve existir para o apetite de risco e necessidades do negócio.
- **Priorização e melhoria**: usar lacunas para montar um roadmap baseado em risco.

[Referência Utilizada](https://csrc.nist.gov/pubs/cswp/29/final)

### Como utilizar CSF?
1) **Definir escopo e contexto a ser aplicado**
   - processos e sistemas críticos, requisitos regulatórios, ambiente a ser implementado (envolve cloud, IoT?).
2) **Perfil Atual**
   - mapear políticas, processos, ferramentas, métricas e evidências por resultados.
3) **Avaliar risco e lacunas existentes**
   - ameaças, vulnerabilidades, impacto, probabilidade; dependências e terceiros envolvidos.
4) **Definir Perfil pretendido**
   - resultados pretendidos (curto/médio prazo) e justificativas.
5) **Roadmap**
   - iniciativas, custos, responsáveis, prazos e  dependências.
6) **Medição e governança**
   - Uso de indicadore como KPIs,revisões, auditorias e lições aprendidas de projetos em andamento.

### Entregáveis recomendados (CSF)
- Inventário de ativos e serviços críticos (incluindo terceiros críticos).
- Perfil CSF Atual e Perfil CSF pretendido (com critérios de avaliação).
- Matriz de lacunas + priorização (risco x esforço x impacto).
- Roadmap trimestral/semestral.
- Conjunto de métricas (operacionais e executivas).

---

## NIST SP 800-53(r5) (controles de segurança e privacidade)

O NIST SP 800-53 Rev. 5 pode ser considerado como um catálogo de controles para segurança e privacidade que é amplamente utilizado no governo federal dos EUA e também por organizações privadas como referência de boas práticas.

[Referência utilizada](ttps://csrc.nist.gov/pubs/sp/800/53/r5/final)

### Conceitos essenciais (didáticos)
- **Controle**: requisito/atividade para reduzir risco (administrativo, técnico e/ou físico).
- **Famílias de controles**: agrupamentos por controle de acesso, resposta a incidnete, proteção de comunicação e sistemas, entre outros controles.
- **Conjuntos iniciais e ajustes necessários**:
  - seleção de um conjunto inicial (baseline) e ajustes conforme contexto e risco.
- **Evidência**:
  - documentação (políticas, padrões/normas e procedimentos),
  - evidência técnica (logs, configurações e relatórios de ferramenta),
  - evidência operacional (registros de execução, exercícios, atas, tickets).



- **NIST SP 800-37 Rev. 2 (RMF)**: estrutura o ciclo de vida (categorizar, selecionar, implementar, avaliar, autorizar, monitorar).
  - https://csrc.nist.gov/pubs/sp/800/37/r2/final

- **NIST SP 800-53A Rev. 5**: procedimentos/métodos para avaliar controles.
  - https://csrc.nist.gov/pubs/sp/800/53a/r5/final

Algumas referências correltas:
- **NIST SP 800-30 Rev. 1 (Risk Assessment)**:
  - https://csrc.nist.gov/pubs/sp/800/30/r1/final
- **NIST SP 800-39 (Enterprise Risk Management)**:
  - https://csrc.nist.gov/pubs/sp/800/39/final


---

## FISMA (Federal Information Security Modernization Act)

A FISMA é a lei dos EUA que estabelece requisitos para programas de segurança da informação nas agências federais, com foco em:
- gestão de risco,
- responsabilidades claras,
- supervisão,
- relatórios e melhoria contínua.

Referência:
- FISMA background (NIST): https://csrc.nist.gov/projects/risk-management/fisma-background


### Atores e responsabilidades (alto nível)
- **Agências**: implementam e operam o programa.
- **NIST**: publica padrões/diretrizes técnicas e metodológicas.
- **Empresas de Auditoria**: realizam auditorias e avaliações independentes.

---

## CSF vs 800-53 vs FISMA

### CSF
- Natureza: framework de outcomes e gestão.
- Objetivo: comunicar, organizar e priorizar o programa.
- Entregáveis: perfis (atual/alvo), lacunas, roadmap e indicadores.

### NIST SP 800-53 Rev. 5
- Natureza: catãlgo detalhado de controles.
- Objetivo: orientar implementação e avaliação de controles (segurança e privacidade).
- Entregáveis: seleção de controles e plano de evidências. 

### FISMA
- Natureza: lei (governo federal EUA).
- Objetivo: exigir programa de segurança baseado em risco, governança e auditoria/relatórios.
- Entregáveis: políticas institucionais, relatõrios executivos, auditorias e planos de ação/correção.

---

## Referências utiizadas 

NIST Cybersecurity Framework (portal):
- https://www.nist.gov/cyberframework

NIST CSF 2.0 (final):
- https://csrc.nist.gov/pubs/cswp/29/final

NIST SP 800-53 Rev. 5 (final):
- https://csrc.nist.gov/pubs/sp/800/53/r5/final

NIST SP 800-37 Rev. 2 (RMF):
- https://csrc.nist.gov/pubs/sp/800/37/r2/final

NIST SP 800-53A Rev. 5 (avaliação de controles):
- https://csrc.nist.gov/pubs/sp/800/53a/r5/final

NIST SP 800-30 Rev. 1 (Risk Assessment):
- https://csrc.nist.gov/pubs/sp/800/30/r1/final

NIST SP 800-39 (gestão de risco organizacional):
- https://csrc.nist.gov/pubs/sp/800/39/final

FISMA background (NIST):
- https://csrc.nist.gov/projects/risk-management/fisma-background

Texto legal (Congress.gov — FISMA Modernization Act):
- https://www.congress.gov/bill/113th-congress/senate-bill/2521

---
## Teste os seus conhecimentos
-[Algumas perguntas sobre o que vimos aqui](https://mehranmisaghi.github.io/cybersecurity/materiais/csfq.html)

# O que vamos aprender agora?
- [Teste de Invasão em Redes (I)](/Codes/pentest.md)