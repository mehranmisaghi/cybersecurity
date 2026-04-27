---
title: 'AES - Questões de revisão'
description: 'Criptografia (II) - AES'
permalink: AES.md
---
# Algumas questões sobre AES

## Disciplina: Segurança da Informação
> Estas questões foram geradas com auxílio de IA e revisadas/alteradas por Mehran Misaghi.
---

## Questão 1 — Estrutura Interna e Rodadas

O AES opera sobre uma estrutura matricial de bytes chamada *State* (Estado) e processa os dados em um número fixo de rodadas, que varia conforme o tamanho da chave utilizada.

**Responda:**

a) Qual é o formato da matriz de *State* utilizada pelo AES e como os bytes do bloco de entrada são organizados nela?

b) Explique a relação entre o tamanho da chave (128, 192 e 256 bits) e o número de rodadas executadas pelo algoritmo. Existe alguma diferença em termos de graua de segurança?

c) Diferencie o que ocorre na **rodada inicial**, nas **rodadas intermediárias** e na **rodada final**, detalhando quais transformações são aplicadas (ou omitidas) em cada fase.

---

## Questão 2 — Avaliação de sistemas criptográficos


a) Explique como utilizar **Compressão de dados** para avaliar um sistema criptográfico. Justifique sua resposta baseada em exemplos.

b) Em que situação um arquivo compactado será maior do que um arquivo não compactado?

c) Caso não seja possível compactar um arquivo (taxa de 0%), o que podemos concluir?

d) Explique como funciona o SAC. 

e) Faça um programa para rotacionamento de um bit de entrada de um arquivo.

---


## Questão 4 — Escalinamento de Chave (Key Schedule)

a) Qual é o objetivo do processo de **Key Schedule** no AES?

b) Descreva as funções **RotWord**, **SubWord** e a constante **Rcon** no processo de geração das sub-chaves.

c) Explique os riscos de segurança caso o algoritmo utilizasse a mesma chave em todas as rodadas ou não utilizasse a constante Rcon.

---

## [Voltar](README.md)