# Resumo de Modelos de Criptografia de Chave Pública Alternativos

> Este resumo foi gerado por IA a partir do [Minicurso ministrado em SBSeg 2009](https://books-sol.sbc.org.br/index.php/sbc/catalog/view/99/442/713)
---

## 1. INTRODUÇÃO E CONTEXTUALIZAÇÃO DO PROBLEMA

A segurança da informação em redes abertas baseia-se historicamente nos fundamentos da Criptografia de Chave Pública, operada na grande maioria dos casos por uma Infraestrutura de Chaves Públicas (ICP). No modelo ancorado no padrão X.509, a vinculação entre a identidade de um usuário e a sua correspondente chave pública é atestada por meio de um certificado digital emitido por uma Autoridade Certificadora (AC). Embora a arquitetura X.509 ofereça considerável estrutura de confiança, o rigor exigido para sua manutenção traz gargalos operacionais e computacionais expressivos: necessidade de repositórios massivos, exigência de banda contínua para downloads de Listas de Certificados Revogados (CRLs) ou interações constantes com protocolos online de verificação de status (OCSP). 

Com a inserção e crescimento de redes ad-hoc, comunicação móvel tolerante a atrasos (DTN) e a proliferação de ambientes restritos, o alto custo computacional do gerenciamento de certificados tornou-se impeditivo. Diante deste cenário, a criptologia moderna buscou novos paradigmas. O documento analisado explora profundamente a evolução desses modelos não convencionais: a Criptografia Baseada em Identidade (IBE), Modelos Autocertificados, a Criptografia Sem Certificados (Certificateless) e a Criptografia Baseada em Certificado (CBE). Cada um destes modelos tenta, à sua própria maneira, mitigar os trâmites burocráticos e os custos de infraestrutura de certificados sem abrir mão das garantias plenas de segurança e irretratabilidade exigidos em trocas seguras de informações.

---

## 2. CRIPTOGRAFIA DE CHAVE PÚBLICA BASEADA EM IDENTIDADE (IBE)

### 2.1 Conceitos Fundamentais
A Criptografia Baseada em Identidade, ou Identity-Based Encryption (IBE), foi proposta inicialmente por Adi Shamir em 1984. O conceito matricial deste paradigma estabelece que a própria identidade individual do usuário (seu número de CPF, seu endereço de e-mail, telefone ou qualquer string unívoca) pode ser matematicamente convertida e interpretada como a sua Chave Pública. Uma Autoridade de Confiança (Geradora de Chaves - AC/PKG) recebe a identidade e, com o uso de um segredo mestre, produz e entrega o respectivo bloco decodificador privado ao requerente.

Neste esquema, a chave pública e a respectiva certificação são dadas intuitivamente: caso o remetente confie na Autoridade, ele assume inatamente que a chave associada àquele ID é válida. Assim, há **certificação implícita**, contornando a integralidade ciberfísica e de arquivamento dos arranjos da ICP tradicional. 

### 2.2 Vantagens Pragmáticas do Modelo
O sistema de ID-based (Baseado em Identidade) ostenta prós singulares:
1. **Dispensa Completa de Diretórios:** Uma chave pública formulada por uma string memorizável elide a demanda do transmissor procurar servidores para baixar e cruzar os arquivos. 
2. **Cifragem Precoce ou Assíncrona:** Diferente das exigências engessadas da técnica tradicional — onde quem deseja receber mensagens cifradas precisa, mandatoriamente, ter se antecipado, gerado uma chave e certificado na AC —, o transmissor em IBE pode criptografar todo o fluxo voltado ao endereço 'bob@empresa.com' ou CPF específico, antes sequer de Bob tomar conhecimento do sistema e dar entrada na produção do arquivo de decifragem.
3. **Escalamento em Grupos Fechados:** A proposta preza pelo uso de sistemas fechados. Matrizes corporativas como Multinacionais, Redes Bancárias e Forças Armadas beneficiam-se estruturalmente como aponta Shamir, pois todos os filiados confiam numa gerência hierárquica e dispensam gastos altos num ecossistema de listagens revogatórias contínuas.

### 2.3 Custódia de Chaves (Key Escrow) e as Fissuras do IBE
O que torna o modelo prático embute também o seu "Calcanhar de Aquiles" irreversível, caracterizado largamente no modelo como "Custódia de Chave" ou *Key Escrow*. 

Segundo o documento analisado e com base em restrições categorizadas por Girault (1991), o IBE coloca o emissor e o utilizador sob a vigência do "Nível 1 de Confiança". Como todo segredo de destravamento emerge inseparavelmente pelas mãos do centro unificador do sistema (a Autoridade da rede), nada inviabiliza física ou computacionalmente esta AC de promover varreduras internas aos pacotes e abrir todo o pacote particular (bisbilhotagem passiva ou ativa). Ela forja identidades falsas transparecendo a gênese, impossibilitando garantias sólidas nos critérios de não repúdio e irretratabilidade perante disputas legais. 

Outras fraquezas e limitações pesadas pontuadas pelos acadêmicos e estudiosos que permeiam esse método abarcam:
1. **O Colapso da Chave Mestra:** Vazada a chave da Autoridade no arquétipo Padrão, emite-se um "Stop" na validação dali por diante e as trocas futuras caem, porém garantindo que as operações encriptografadas pretéritas do ambiente seguem insólitas. Com IBE, contudo, qualquer invasor ganha poderes oniscientes e decifra dados do instante transcorrido ao nascedouro, destruindo retroativamente toda integridade criptográfica já construída da base. 
2. **Canais de Distribuição de Alta Segurança Exigida:** Requer banda estrita protegida presencial ou encriptada prévia perante as pontas, gerando os nós e repassando o material sem corrompê-los na superfície comunicativa. 
3. **O Dilema de Cancelamento Pessoal (Revogação):** É imperioso no mundo ciberfísico banir uma porta exposta. Perder senhas IBE, pautadas em atributos perenes como "CPF", tranca soluções fáceis. O alívio de autores mais pragmáticos foca em amarrar concatenações cronológicas, como `JoãoSilva-Setembro2009`. Mas se a granularidade temporal estreitar demais para melhorar a responsividade de evasão contra brechas, o peso logístico cai vertiginosamente sob os servidores da Autoridade re-emitindo credenciais por janelas cadentes curtíssimas. Recentemente, visando soluções avançadas perante isto, arquiteturas com tempo computacional revogatório decrescente alcançando a linha de complexidade logarítmica emergiram conforme Boldyreva et al. (2008), opondo-se à métrica de lentidão estrutural e linear de outrora. Similarmente, na contenção pontual da custódia maliciosa, a proteção via disfarce de receptor de esquema e anonimização em rede aberta é explorada amplamente por Chow (2009).

### 2.4 Esquemas Genéricos e Concretização Sistêmica (Boneh e Franklin)
Expondo em minúcias matemáticas propostas na criptografia das últimas duas décadas, o manuscrito apóia a base conceitual dos estudos de Assinatura por Identidade (IBS) e Criptografia (IBE) nos emparelhamentos de curvas lineares. O esquema revolucionário de IBE concreto demonstrado por **Boneh e Franklin (2001)** consolida as abstrações.

Possuindo **quatro fases delineatórias estruturais contíguas:** 
- **Inicializa:** Submetido um limite e parâmetros de segurança ($k$), gera-se a chave mestra algorítmica ($s$) onde os parâmetros abertos do sistema tornam-se de amplo saber público ("$params$"), onde os grupos operacionais adotam ordem prima em espaços abertos bilineares ($G_1$ e $G_2$) sob o emparelhamento permissível de $e: G_1 \times G_1 \to G_2$. 
- **Extrai:** De posse de parâmetros como $ID_{A}$ ($A$ da rede) e as variáveis hash predeterminadas do sistema principal, a AC apura o segredo do destinatário calculando a derivada com seu "s" íntimo para formar o bloco privado $d_A = s Q_A$. 
- **Cifra:** Emissor insere texto legível, converte contra os vetores hash da chave da corporação e ao identificador puro. Transmite um pacote blindado ao exterior com variáveis ininteligíveis computadas. 
- **Decifra:** O Titular intercepta o bloco, empurra as frações exclusivas ao processador contra as amarras de grupo das curvas elípticas ($e(d_A, U)$) extraindo com o pareamento do subjacente secreto as correntes originárias puras, abortando caso hashes e blocos de segurança sejam divergentes indicando fraude injetada. 

Há construções alheias aos emparelhamentos, como a notória matriz de Cocks (2001) lastreada sobre a difícil resolução matemática dos problemas de resíduos quadráticos. Contudo, devido a um severo inchaço informacional derivado (grande expansão do texto cifrado de saída em byte logístico), obteve atenção tardia com readequações apenas recentes (Boneh et al., 2007). 

---

## 3. CRIPTOGRAFIA DE CHAVE PÚBLICA AUTOCERTIFICADA 

### 3.1 Prova de Posse e Conhecimento
Distanciando a ciência e a confiança exacerbada perante o nó-chave das entidades certificadoras, Marc Girault pavimenta em 1991 um modelo teórico focado em mitigar o assustador desequilíbrio das responsabilidades em posse no arcabouço original de Shamir.

Conhecido como Criptografia Autocertificada (Self-Certified), o arcabouço dita obrigações onde o próprio proponente adquire e assume um fragmento formador puramente randômico e intransferível de suas entranhas. Perante a AC, durante as tratativas de geração, opera-se provas tangentes ao Conceito de Zero-Knowledge (Conhecimento-Zero). Nenhum polo entrega seu núcleo inviolável ao outro. Como resultado líquido primordial a ser sublinhado, encerra-se o dilema de vigilância oculta ("Key Escrow"); a instituição centralizadora despede-se totalmente da engrenagem de clonagem e monitoramento de correspondência passiva pois dispõe de fração parcial que nada gera sem o fragmento de completude individual do operador nativo.

Na essência, para o usuário ou máquina atestar que a chave foi forjada sob escopo real sem ICP engessada e dispendiosa, adota-se "Certificação Implícita", garantida retrospectivamente frente o processamento sem quebra dos protocolos. A inviabilidade de transcrever a mensagem recebida prova a ausência de domínio em cadeia fechada.

### 3.2 Otimização de Dupla Verificação (Cenários Práticos)
Uma desvantagem pragmática encontrada no ambiente regular é o gargalo cumulativo durante a legitimação de inúmeras frentes. Para atestarmos material recebido sob X.509, duas assinaturas onerosas encadeiam-se antes nos microprocessadores (Validar assinatura institucional do Certificado, seguido, extraída a raiz pública, validar a assinatura contida na peça documental referendada). Lee e Kim (2002) mitigaram a superposição usando Autocertificação nos meios tradicionais sem duplo passo com recálculo nativo local otimizado.

Ademais, grandes marcas integradoras da Cibersegurança exploraram esses atalhos valiosos economicamente viáveis à largura de banda. Citada pelo documento base, a Certicom (associada também a matrizes operárias de comunicação ZigBee e processabilidade de fronteira Smart Energy) usa arquiteturas patenteadas por ECQV onde as variáveis implícitas processadas dispensam arquivos volumosos a favor da mera remanufatura atestatória barata em IoTs, nós com microcontroladoras sub-dimencionadas e equipamentos contidos restritamente na "Edge".

---

## 4. CRIPTOGRAFIA SEM CERTIFICADOS (CERTIFICATELESS PUBLIC KEY CRYPTOGRAPHY - CL-PKC)

### 4.1 A Reconciliação dos Fragmentos Intermediários 
A gênese deste esquema baseia-se num esforço literário e programático robusto consolidado por Al-Riyami e Paterson (2003). As premissas são evidentes: manter as altas efiências livres de burocracias pesadas presentes do modelo de IBE sem retroceder e resgatar um certificado ICP atrelado, banindo sumariamente, na premissa, o controle governamental ou corporativo extremo custodiado sob o modelo central ("eliminating key escrow").

A engenharia sem certificado quebra, portanto, parte da simplicidade purista. Uma Autoridade base calcula a chave secreta parcial acoplada as variáveis abertas unívocas; repassa secretamente ao destinatário que embute o próprio "segredo de sistema local". Juntos o resultado forma integralmente uma nova identidade (a Chave Pública livre das amarras governamentais algoritmizadas da firma matriz). Tal conformação possibilita atualizações modulares descentralizadas locais onde múltiplos polos podem conviver ativamente, descartados o envio das listagens onipresentes de renovações e caducidade da agência superior.

#### Operacionalização Interna da Matriz (Segundo a Base do Esquema Genérico de Geradores)
No protocolo interno subentendido do modelo de Al-Riyami (usando frações computacionais):
1. **Pela Autoridade:** Produz-se um Hash basilar da designação do associado: $Q_A = H_1("A")$. Da identidade extrai o parcial privado com seus dados estritos ($d_A = s Q_A$).
2. **Pelo Indivíduo Final (Client Side):** Um fator isolado, genuíno, estocástico de bits complexos é convocado num randomizador ($s_A \in Z^*_q$). Consecutivamente, monta seu corpo de transmissão público ($P_A = s_A Q$). Somente sob esses arranjos a decifragem real torna-se hábil.

### 4.2 Adversários Avaliados e Níveis de Confiança Tático Computacionais
Nas delimitações analíticas dos proponentes, duas vertentes prementes de ataques foram dispostas metodologicamente e os esquemas devem assegurar resistência de ordem irrisória de acertos a quem tentar forjá-las nos simuladores:
*   **Adversário Tipo 1 (Ameaça Descentralizada Externa):** Usuários autônomos ilícitos com propensões operativas plenas onde forjam a chave pública disponível e substituem na teia as veracidades associadas a contatos paralelos. 
*   **Adversário Tipo 2 (Autoridade Interna Maliciosa):** Entidade Honesta e Vigilante que repara e fareja material perambulante nas redes, porém ausente das frações confusas e locais estipuladas individualmente pelo terminal externo.

Sob tal prisma, o modelo habita tradicionalmente o estuário de "Nível 2 de Segurança" da escala padrão. Exceção recai sobre casos flagrantemente mal-intencionados como provados pelos pesquisadores subjacentes onde Au et al. (2007) demonstra fraquezas de instâncias centrais gerando atalhos desonestos durante o emparelhamento raiz do sistema de dados base contornando sem aviso todo arcabouço preventivo arquitetado por Al-Riyami. As proteções preventivas advindas em resoluções recentes contra autoridades mal intencionadas contam com os escudos baseados num leque de equações propostas por Dent (2008) e Hwang et al. (2008)

### 4.3 Ataques Denial of Decryption (DoD) e Dificuldades Adjacentes
Apesar de atrativo, os críticos ressaltam de imediato e em uníssono a vulnerabilidade tática assinalada da falta de certificados sob publicações difusas e abertas: **O Ataque de Negação de Serviço Criptográfico**. Apelidado explicitamente como Ataque DDoS Criptográfico, referenciado pelos estames de "Denial of Decryption - DoD" (Liu et al. 2007). 

Como há publicidade livre e falta certificações impositivas que amparem a confiabilidade orgânica na camada superior, atacantes virtuais desconfiguram os dados reposicionados livremente nos sub-diretórios de contatos e repositórios paralelos colocando seus fragmentos na camada da variável $P_A$, vinculando terceiros em armadilhas de fluxo passivo. Terceiros embalam conteúdo usando chave alterada de Alice; o pacote entra numa rua sem saída ao repousar contra o cálculo intransponível da secretividade contida em base nos processadores nativos de destino, negando atestabilidade às assinaturas expostas legalmente ao público falhando e invalidando interações e, mais grave, ocultando a gênese destas sabotagens das percepções rápidas de resposta sistêmica contra desastres gerados nos fluxos diários. Tentativas elaboradas na camada temporal para corrigir essa brecha de validação implícita infelizmente tendem a inserir assinaturas recursivas na documentação retroagindo e engessando exatamente aquilo que prometeram afrouxar inicialmente.

---

## 5. CRIPTOGRAFIA BASEADA EM CERTIFICADOS (CERTIFICATE-BASED ENCRYPTION - CBE)

### 5.1 Restabelecimento Certificado como Assinatura Integrada Discreta
Percebendo as oscilações e incertezas quanto aos diretores das propostas sem certificação, Gentry avança à frente com forte contribuição publicando seu manual extensivo em 2003: Criptografia Baseada em Certificados (CBE). Diferentemente do purismo e de se abster de assinaturas e órgãos de controle normativos, esse modelo mantém intrinsecamente ativa toda malha física de Autoriades Certificadoras tal qual vivenciado hoje no modelo X.509 mundial, inclusive atrelando cadeias perfeitamente dispostas na topologia e raízes superiores (CAs e Root-CAs).

A premissa da tese e de toda sua lógica propulsora e avassaladora mudança algorítmica dá-se na extinção da conferência on-line (excesso oneroso sob validação das listas e nós validados OCSPs contínuos à exaustão por dezenas de milhões na hora estipuladas nos data centers, referindo falência ou ineficiências em emissões girando acima de 225 milhões de certificados na base aferida de Gentry pelo processador de tempo da máquina centralizada).

Aqui, a submissão dos certificados funciona agregada secretamente junto à base nativa individual na arquitetura formacional, embutindo temporalidade e cronogramas (por exemplo, período variável estipulado $i$ - validos na fração hora ou mês).

### 5.2 Decifragem Condicionada à Atualização Conjunta
Nesse ínterim submetido, para firmar trâmites ou extrair fidedignamente blocos alheios criptografados o sistema precisa amarrar na execução interna duas validações matemáticas acopladas obrigatoriamente: o componente orgânico privado impenetrável de criação da assinatura e, adicionalmente, ter baixado ou obtido e armazenado individualmente (não retransmitido para avaliação universal constante) a assinatura/certificado perante a matriz superior daquele ciclo $i$ específico limitador programático; não portando a fração atualizada e em dia em posse própria temporalmente atrelada por trás da blindagem processadora inviabilizará o acoplamento final.

A submissão dessa logística recai singularmente às costas isoladas do utilizador focado (diminuindo assim em grandeza imensurável os inchaços sistêmicos da validação macro rede universal); terceiros emissários dispensam verificação perante a autoridade sobre os dados da assinatura digital recebida de Alice em CBE, procedendo a encriptação combinada pautada tacitamente sob os regimentos restritivos e perfeitamente equilibrados onde a identidade e as equações implícitas validam seguranças inquebráveis e robustas do próprio modelo de Emparelhamento. A robustez frente a ameaças assegura conformações enquadradas no Nível 3 de Segurança em contraposição a IBE purista devido possiblidade exaustiva imposta e incontornável da não revogação sem evidência de fraudes passíveis da extração retroativa nas eventuais disputas. 

A formatação original e seus aprimoramentos subsequentes — como as variantes CBE de complexo modelo demonstrativo formal por Lu et al. (2009) suportada sob oráculos padronizados ou modelos eficientes provados e agregados baseados sob teorizações estáticas da complexidade como aponta o extenso compêndio sob Kang, Dodis e correntes provadoras estritas de adversário forte para Assinaturas (onde adversário injeta forçadamente simulações na base e só prosperaria se a agência subornar os sistemas validatórios das CAs com assinaturas não lícitas - Li et al., 2007) formaram consolidações incontestáveis ao ciber-ambiente em maturidade de pesquisas correntes. 

---

## 6. CONCLUSÃO

A literatura sobre evolução da segurança transacionada abarca avanços profundos baseados em desconstruir premissas monolíticas clássicas de burocracias sob validade digital estagnadas. Desde o desvelar simples e prático — porém inviável nas garantias restritivas corporativas —, advindos de Shamir (1984) repousado unicamente sob os atributos da pessoa como base aberta de conversão sem privacidade local impenetrável; à blindagem do titular através das Autocertificações modulares de Girault forrando o detentor e o poupando da custódia irrefreável centralizadora e vigilante; até à prospecção do esquema focado em Criptossistemas Isentos de Validações Certificadas explícitas arquitetadas metodologicamente por Al-Riyami, suportadas infelizmente por fragilidades subjacentes focadas nos desastres de negação de decifragem difusos explorados na superfície. Por fim alcançando em Gentry (2003) e nas modelagens amadurecidas matemáticas embasadas estritamente e demonstradas fortes (sob hipóteses não arbitrárias dos modelos de oráculo) nos construtos com o Modelo Baseado na emissão local do Certificado (CBE). As construções demonstram invariavelmente uma balança tênue regrada constantemente contra adversários virtuais internos e externos num estrito balé focando recursos escassos de memórias e limites matemáticos onde, se devidamente parametrizados perante à malha real das instâncias, tornam segura toda sociedade regida computacionalmente.

---

## 7. REFERÊNCIAS

**ABDALLA, M. et al.** Identity-based encryption gone wild. In: INTERNATIONAL COLLOQUIUM ON AUTOMATA, LANGUAGES AND PROGRAMMING (ICALP), 33., 2006, Veneza. **Lecture Notes in Computer Science**, Berlin: Springer-Verlag, v. 4052, p. 300–311, 2006.

**ABDALLA, M. et al.** Searchable encryption revisited: consistency properties, relation to anonymous IBE, and extensions. **Journal of Cryptology**, v. 21, n. 3, p. 350–391, 2008.

**AL-RIYAMI, S. S.** **Cryptographic Schemes based on Elliptic Curve Pairings.** 2005. Tese (Doutorado) – Department of Mathematics, Royal Holloway, University of London, Londres, 2005.

**AL-RIYAMI, S. S.; PATERSON, K. G.** Certificateless public key cryptography. In: INTERNATIONAL CONFERENCE ON THE THEORY AND APPLICATION OF CRYPTOLOGY AND INFORMATION SECURITY (ASIACRYPT), 9., 2003, Taipei. **Lecture Notes in Computer Science**, Berlin: Springer, v. 2894, p. 452–473, 2003.

**AL-RIYAMI, S. S.; PATERSON, K. G.** CBE from CL-PKE: a generic construction and efficient schemes. In: INTERNATIONAL WORKSHOP ON PUBLIC KEY CRYPTOGRAPHY (PKC), 8., 2005, Les Diablerets. **Lecture Notes in Computer Science**, Berlin: Springer, v. 3386, p. 398–415, 2005.

**APPENZELLER, G.; LYNN, B.** Minimal-overhead IP security using identity-based encryption. 2002. Universidade Stanford. Disponível online.

**ASOKAN, N. et al.** Applicability of identity-based cryptography for disruption-tolerant networking. In: ACM WORKSHOP ON MOBILE OPPORTUNISTIC NETWORKING (MobiOpp), 1., 2007, San Juan. **Proceedings...** New York: ACM, 2007. p. 52–56.

**AU, M. H. et al.** Certificate based (linkable) ring signature. In: INTERNATIONAL CONFERENCE ON INFORMATION SECURITY PRACTICE AND EXPERIENCE (ISPEC), 3., 2007. **Lecture Notes in Computer Science**, Berlin: Springer, v. 4464, p. 79–92, 2007.

**AU, M. H. et al.** Malicious KGC attacks in certificateless cryptography. In: ACM SYMPOSIUM ON INFORMATION, COMPUTER AND COMMUNICATIONS SECURITY (ASIACCS), 2., 2007, Singapura. **Proceedings...** New York: ACM, 2007. p. 302–311.

**BAEK, J. et al.** A survey of identity-based cryptography. In: AUUG CONFERENCE, 2004, Melbourne. **Proceedings...** Oztalia, 2004. 

**BAEK, J.; SAFAVI-NAINI, R.; SUSILO, W.** Certificateless public key encryption without pairing. In: INTERNATIONAL CONFERENCE ON INFORMATION SECURITY (ISC), 8., 2005, Singapura. **Lecture Notes in Computer Science**, Berlin: Springer, v. 3650, p. 134–148, 2005.

**BOLDYREVA, A. et al.** Identity-based encryption with efficient revocation. In: ACM CONFERENCE ON COMPUTER AND COMMUNICATIONS SECURITY, 2008. **Proceedings...** Nova York: ACM, p. 417-426, 2008.

**BONEH, D.; BOYEN, X.** Efficient selective-ID secure identity-based encryption without random oracles. In: INTERNATIONAL CONFERENCE ON THE THEORY AND APPLICATIONS OF CRYPTOGRAPHIC TECHNIQUES (EUROCRYPT), 23., 2004, Interlaken. **Lecture Notes in Computer Science**, Berlin: Springer, v. 3027, p. 223–238, 2004.

**BONEH, D.; FRANKLIN, M.** Identity-based encryption from the Weil pairing. In: ANNUAL INTERNATIONAL CRYPTOLOGY CONFERENCE (CRYPTO), 21., 2001, Santa Bárbara. **Lecture Notes in Computer Science**, Berlin: Springer, v. 2139, p. 213–229, 2001.

**BONEH, D. et al.** Aggregate and verifiably encrypted signatures from bilinear maps. In: INTERNATIONAL CONFERENCE ON THE THEORY AND APPLICATIONS OF CRYPTOGRAPHIC TECHNIQUES (EUROCRYPT), 22., 2003, Varsóvia. **Lecture Notes in Computer Science**, Berlin: Springer, v. 2656, p. 416–432, 2003.

**CHOW, S. S. M.** Removing escrow from identity-based encryption. In: INTERNATIONAL WORKSHOP ON PUBLIC KEY CRYPTOGRAPHY (PKC), 12., 2009. **Lecture Notes in Computer Science**, Berlin: Springer, 2009.

**CHOW, S. S. M.; BOYD, C.; NIETO, J. M. G.** Security-mediated certificateless cryptography. In: INTERNATIONAL WORKSHOP ON PUBLIC KEY CRYPTOGRAPHY (PKC), 9., 2006, Nova York. **Lecture Notes in Computer Science**, Berlin: Springer, v. 3958, p. 508–524, 2006.

**COCKS, C.** An identity based encryption scheme based on quadratic residues. In: IMA INTERNATIONAL CONFERENCE ON CRYPTOGRAPHY AND CODING, 8., 2001, Londres. **Lecture Notes in Computer Science**, Berlin: Springer, v. 2260, p. 360–363, 2001.

**CRAMPTON, J.; LIM, H. W.; PATERSON, K. G.** What can identity-based cryptography offer to web services? In: ACM WORKSHOP ON SECURE WEB SERVICES (SWS), 4., 2007, Fairfax. **Proceedings...** New York: ACM, 2007.

**DENT, A. W.** A survey of certificateless encryption schemes and security models. **International Journal of Information Security**, v. 7, n. 5, p. 349–377, 2008.

**DODIS, Y.; KATZ, J.** Chosen-ciphertext security of multiple encryption. In: THEORY OF CRYPTOGRAPHY CONFERENCE (TCC), 2., 2005. **Lecture Notes in Computer Science**, Berlin: Springer, v. 3378, p. 188–209, 2005.

**GENTRY, C.** Certificate-based encryption and the certificate revocation problem. **Cryptology ePrint Archive**, Report 2003/183, 2003. 

**GENTRY, C.; SILVERBERG, A.** Hierarchical ID-based cryptography. In: INTERNATIONAL CONFERENCE ON THE THEORY AND APPLICATION OF CRYPTOLOGY AND INFORMATION SECURITY (ASIACRYPT), 8., 2002, Queenstown. **Lecture Notes in Computer Science**, Berlin: Springer, 2002.

**GIRAULT, M.** Self-certified public keys. In: INTERNATIONAL CONFERENCE ON THE THEORY AND APPLICATIONS OF CRYPTOGRAPHIC TECHNIQUES (EUROCRYPT), 1991. **Lecture Notes in Computer Science**, Berlin: Springer, 1991.

**HESS, F.** Efficient identity based signature schemes based on pairings. In: INTERNATIONAL WORKSHOP ON SELECTED AREAS IN CRYPTOGRAPHY (SAC), 9., 2002. **Lecture Notes in Computer Science**, Berlin: Springer, v. 2595, p. 310–324, 2003.

**JOUX, A.** A one round protocol for tripartite Diffie-Hellman. In: INTERNATIONAL ALGORITHMIC NUMBER THEORY SYMPOSIUM (ANTS), 4., 2000, Leiden. **Lecture Notes in Computer Science**, Berlin: Springer, v. 1838, p. 385–393, 2000.

**LIU, J. K. et al.** A secure certificateless signature scheme. In: IEEE SMC, 2007.

**MISAGHI, M.** **Um Ambiente Criptográfico Baseado na Identidade.** 2008. Tese (Doutorado) – Escola Politécnica, Universidade de São Paulo, São Paulo, 2008.

**NACCACHE, D.** Secure and practical identity-based encryption. **IET Information Security**, v. 1, n. 2, p. 59–64, 2007. 

**PETERSEN, H.; HORSTER, P.** Self-certified keys: concepts and applications. In: COMMUNICATIONS AND MULTIMEDIA SECURITY CONFERENCE, 3., 1997. **Proceedings...** p. 102–116, 1997.

**SAKAI, R.; KASAHARA, M.** ID based cryptosystems with pairing on elliptic curve. **Cryptology ePrint Archive**, Report 2003/054, 2003. 

**SHAMIR, A.** Identity-based cryptosystems and signature schemes. In: ANNUAL INTERNATIONAL CRYPTOLOGY CONFERENCE (CRYPTO), 4., 1984, Santa Bárbara. **Lecture Notes in Computer Science**, New York: Springer-Verlag, v. 196, p. 47–53, 1984.

**TRAPPE, W.; WASHINGTON, L. C.** **Introduction to Cryptography with Coding Theory.** 2. ed. Upper Saddle River: Prentice Hall, 2005.

**WATERS, B. R.** Efficient identity-based encryption without random oracles. In: INTERNATIONAL CONFERENCE ON THE THEORY AND APPLICATIONS OF CRYPTOGRAPHIC TECHNIQUES (EUROCRYPT), 24., 2005. **Lecture Notes in Computer Science**, Berlin: Springer, v. 3494, p. 114–127, 2005.

**ZHANG, Z. et al.** Certificateless public key signature: security model and efficient construction. In: INTERNATIONAL CONFERENCE ON APPLIED CRYPTOGRAPHY AND NETWORK SECURITY (ACNS), 4., 2006, Singapura. **Lecture Notes in Computer Science**, Berlin: Springer, v. 3989, 2006.

**ZHENG, Y.** Digital signcryption or how to achieve cost(signature & encryption) << cost(signature) + cost(encryption). In: ANNUAL INTERNATIONAL CRYPTOLOGY CONFERENCE (CRYPTO), 17., 1997, Londres. **Lecture Notes in Computer Science**, Berlin: Springer-Verlag, p. 165–179, 1997.
