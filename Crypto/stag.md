---
title: 'Esteganografia'
description: 'Esteganografia'
permalink: stag.md
---
# 🕵️ Esteganografia
> Este material foi elaborado com auxílio de IA e revisado por professor.
---
## 1. O que é **esteganografia**?
A palavra **esteganografia** vem do grego:
*   *Steganos* = coberto, escondido
*   *Graphia* = escrita


## 2. Um Pouco de História

A técnica é muito mais antiga que os computadores:

1.  **Grécia Antiga:** Histiaeus raspou a cabeça de um escravo, tatuou uma mensagem no couro cabeludo dele e esperou o cabelo crescer. O escravo foi enviado ao destinatário, que raspou a cabeça do escravo novamente para ler a mensagem.
2.  **Tábuas de Cera:** Escreveu uma mensagem na madeira de uma tábua de escrever antes de cobri-la com cera. A tábua parecia em branco, pronta para uso, passando pelos guardas.
3.  **Tinta Invisível:** Muito usada na Primeira e Segunda Guerras Mundiais (usando suco de limão ou produtos químicos) revelada apenas com calor.
4.  **Micropontos:** Mensagens reduzidas ao tamanho de um ponto final em uma carta comum.

---

## 3. Esteganografia Digital

Atualmente esteganografia conta com recursos digitais para imagem, áudio e vídeo, sendo todos são un conjunto  de zeros e uns (bits). A esteganografia digital geralmente altera os **bits menos importantes** de um arquivo para esconder dados.

### A Técnica LSB (Least Significant Bit - Bit Menos Significativo)

Imagine que a cor de um único pixel em uma imagem seja definida por números de 0 a 255.
*   Valor do Pixel: `250` (Um tom de azul) -> Em binário: `11111010`
*   Se mudarmos o último bit de `0` para `1`, o valor vai para `251` -> `11111011`.

Essa mudança de tom é **impossível** de ser percebida pelo olho humano. Alterando o último bit de vários pixels, podemos escrever o que quisermos dentro da imagem.

### Arquivo Portador (Carrier) vs. Mensagem Oculta (Payload)
*   **Carrier:** O arquivo inocente (uma foto de um gatinho).
*   **Payload:** O que você quer esconder (o texto "A senha é 1234").

---

## 4. Exemplos Práticos sem usar digital (Texto)


### Exemplo 1: Acrósticos (Primeira letra)

Leia a mensagem abaixo:

**S**abemos que o projeto é complexo.
**O**ntem o chefe não aprovou a verba.
**C**ontinuamos trabalhando muito.
**O**rgulho é o que não nos falta.
**R**esolvemos os principais problemas.
**R**euniões constantes ajudaram.
**O**brigado pelo apoio de sempre.

**Mensagem Oculta:** SOCORRO

### Exemplo 2: Padrão de Posição (Ex: A 3ª palavra de cada frase)

Leia a mensagem abaixo:

O cão **vai** pegar o osso amanhã. Ele corre **para** o parque bem cedo. A vizinha costuma **casa** com as janelas abertas.

**Mensagem oculta:** vai para casa.

---

## 6. Usar cifração junto com esteganografia

1. **Cifrar** o arquivo/mensagem com algum cifrador forte. 
2. **Esconder** (Esteganografia) esse arquivo/mensagem cifrado dentro de uma imagem.
Se o invasor desconfiar da imagem e conseguir extrair os dados, ele só encontrará um arquivo cifrado e sem chave, não conseguirá chegar no arquivo/mensagem original!

---
## [Fundamentos de Criptografia e Ferramentas Utilizadas](README.md)
