# Projeto de Segurança II (PSII) 02/06
> Elaborar políticas de segurança da informação com as particulidades de cada cenário
- Cada grupo deve escolher um cenário.
- Para melhor entedimento, revise os conceitos de [Poítica de Segurança e Política de Privacidade](politica.md)

## 1. Centro Hospitalar Digital (CHD) (Maria e Pedro)
É um centro hospitalar que possui prontuário eletrônico integrado com os laboratório e acesso remoto por médicos.

Elabore uma política para abordar:

- Controle de acesso por perfil (médico, enfermeiro(a), administrativo)
- Armazenamento seguro de dados sensíveis (especificar tipo de criptografia)
- Descarte digital de prontuários antigos
- Política de troca de senha obrigatória
- Restrição total de uso de redes sociais em áreas críticas
- Restrição parcial de uso de redes sociais em outras áreas

Não esqueça de tratar:

- Vazamento de dados de pacientes
- Acesso indevido por funcionários
- Uso de redes sociais em ambiente clínico
```mermaid
flowchart LR
A[CHD] --> B[Dados Sensiveis]
A --> C[Usuarios: Medicos e Equipe]
A --> D[Sistemas Integrados]

B --> E[Risco: Vazamento]
C --> F[Risco: Acesso indevido]
D --> G[Risco: Integracao insegura]

E --> H[Politicas de Seguranca]
F --> H
G --> H
```
---
## 2. Agronegócio 4.0 
É uma fazenda inteligente com sensores e drones.

Elabore uma política para abordar:

- Controle de acesso a dispositivos e sistemas
- Armazenamento de dados agrícolas na nuvem (especificar o tipo de criptografia)
- Descarte de dados históricos e backups
- Política de senhas para dispositivos IoT
- Uso de redes sociais por operadores em campo

Não esqueça de tratar:

- Dispositivos IoT vulneráveis
- Dados de produção expostos
- Acesso remoto inseguro
```mermaid
flowchart LR
A[Agronegocio 4.0] --> B[Sensores e Drones]
A --> C[Nuvem]
A --> D[Operadores]

B --> E[Risco: Dispositivo vulneravel]
C --> F[Risco: Interceptacao dados]
D --> G[Risco: Acesso remoto]

E --> H[Politicas de Seguranca]
F --> H
G --> H
```
---
 ## 3. Sistema de Pagamento Digital (SPD)
É ume empresa que processa pagamentos e dados financeiros de clientes.

Elabore uma política para abordar:

- Controle de acesso com autenticação MFA
- Armazenamento seguro (criptografia de dados financeiros - indicar tipo utilizado)
- Descarte seguro de logs e dados sensíveis
- Política de escolha/troca de senha (alta criticidade)
- Uso controlado de redes sociais por funcionários

Não esqueça de abordar:

- Fraudes
- Vazamento de dados financeiros
- Engenharia social via redes sociais
```mermaid
flowchart LR
A[SPD] --> B[Dados Financeiros]
A --> C[Usuarios]
A --> D[Transacoes]

B --> E[Risco: Vazamento]
C --> F[Risco: Fraude]
D --> G[Risco: Ataque cibernetico]

E --> H[Politicas de Seguranca]
F --> H
G --> H
```
---
## 4. EducaOnline (Camila, Gabriel e Sidiclei)
É uma instituição de ensino com cursos online, permitinado acesso online aos seus cursos.

Elaborae uma política para abordar:

- Controle de acesso de alunos e professores (MFA)
- Armazenamento de dados acadêmicos (criptografia - especificar)
- Descarte de dados de ex-alunos
- Política de troca de senha
- Uso de redes sociais dentro da rede institucional

Não esquecer de tratar:
- Compartilhamento indevido de contas
- Vazamento de dados acadêmicos
- Uso indevido da internet
```mermaid
flowchart LR
A[EudcaOnline] --> B[Alunos]
A --> C[Professores]
A --> D[Sistema Academico]

B --> E[Risco: Compartilhamento conta]
C --> F[Risco: Acesso indevido]
D --> G[Risco: Vazamento dados]

E --> H[Politicas de Seguranca]
F --> H
G --> H
```
---
## 5. Sistema de e-commerce
É uma Loja online com dados pessoais e histórico de compras.

Elaborar uma política para tratar:

- Controle de acesso ao sistema administrativo(MFA)
- Armazenamento seguro de dados de clientes (criptografia - especificar)
- Descarte de dados obsoletos
- Política de senha
- Uso de redes sociais para atendimento ao cliente

Não esquecer de tratar:
- Vazamento de dados
- Manipulação de informações
```mermaid
flowchart LR
A[Ecommerce] --> B[Clientes]
A --> C[Pagamentos]
A --> D[Sistema Web]

B --> E[Risco: Vazamento dados]
C --> F[Risco: Fraude]
D --> G[Risco: Ataque web]

E --> H[Politicas de Seguranca]
F --> H
G --> H
```
---
## 6. Órgão Público
É uma instituição governamental com dados de cidadãos.

Elaborar uma política para tatar:

- Controle de acesso por nível hierárquico
- Armazenamento de dados sensíveis (criptografia - especificar)
- Descarte digital conforme legislação
- Política de troca de senha obrigatória
- Uso de redes sociais por servidores públicos

Não esqueça de tratar:

- Vazamento de informações
- Baixa cultura de segurança
- Uso indevido de sistemas
```mermaid
flowchart LR
A[Orgao Publico] --> B[Cidadaos]
A --> C[Servidores]
A --> D[Sistemas]

B --> E[Risco: Dados sensiveis]
C --> F[Risco: Uso indevido]
D --> G[Risco: Falhas sistema]

E --> H[Politicas de Seguranca]
F --> H
G --> H
```
---
## 7. Uma indústria de tubos
É uma fábrica com sistemas industriais conectados à internet.

Elaborar umapolítica que inclua:

- Controle de acesso físico e lógico (segmentado por setor)
- Armazenamento de dados industriais (criptografia - especificar)
- Descarte de logs operacionais
- Política de senha para operadores
- Uso restrito de redes sociais em áreas operacionais

Não esqueça de tatar:

- Acesso indevido à produção
- Risco de sabotagem
- Integração TI x IoT
```mermaid
flowchart LR
A[Industria] --> B[TI]
A --> C[IoT]
A --> D[Operadores]

B --> E[Risco: Integracao TI - IoT]
C --> F[Risco: Sabotagem]
D --> G[Risco: Acesso indevido]

E --> H[Politicas de Seguranca]
F --> H
G --> H
```
---
## Artefatos esperados:
- Entregar o documento de política citando as partes de cada norma utilizada.
- Entregar a tabela de riscos preenchida
- Elaborar uma apresentação
- Apresentar a política elaborada.

## Grupos de Trabalho(02/06)
1. Maria Fernanda e Pedro (CHD)
2. 
3. 
4. 
5. 
6. 
7. 
---
