# Aula TP - 08/Abr/2019
## Exercícios

### 1. Risco
#### Pergunta P1.1

Considerando um PC doméstico e um servidor de *homebanking* de um Banco. O que estará sujeito a um maior risco na Internet será o servidor de _homebanking_ visto que, utilizando as seguintes fórmulas:

```risco = probabilidade de ataque ter sucesso * impacto```

```probabilidade do ataque ter sucesso = nível da ameaça * grau de vulnerabilidade```

Podemos inferir que o ```nível de ameaça``` e o ```impacto``` do servidor de *homebanking* será bastante elevado e que o PC doméstico terá sempre esses valores a um nível menor mesmo tendo um ```grau de vulnerabilidade``` bastante mais elevado do que o servidor. Ou seja, mesmo se a ```probabilidade do ataque ter sucesso ``` fosse a mesma (visto que o ```nível de ameaça``` do servidor é maior do que o nível do PC, e o ```grau de vulnerabilidade``` do PC é maior do que o grau do servidor), o ```impacto``` quando ocorre um ataque com sucesso num servidor de *homebanking* é muito maior do que o ```impacto``` a um ataque sucedido a um PC doméstico porque o primeiro terá informações mais sensível do que o segundo.



### 2. Secure Software Development Lifecycle (S-SDLC)
#### Pergunta P2.1

Modelo de desenvolvimento de software seguro *Microsoft Security Development Lifecycle* tem 7 fases sendo elas: 

- (Pré)Fase de Formação
- Fase de Requisitos
- Fase de Desenho
- Fase de Codificação
- Fase de Verificação
- Fase de Publicação
- (Pós)Fase de Resposta

A Fase de Requisitos contém a Identificação de Requisitos de Segurança tendo esses requisitos dois tipos, políticas de segurança e mecanismos de segurança, sendo que os mesmos são levantados através da legislação aplicável ao negócio, dos *standards*, dos valores e/ou políticas da empresa, dos modelos de risco e dos casos de abuso o que leva à necessidade de usar o regulamento europeu RGPD nesta fase do modelo.
#### Pergunta P2.2

Os controlos de segurança da Secção 10.1 *Cryptographic controls* são:

- ***Policy on the use of cryptographic controls*** - Desenvolvimento e implementação de uma política de uso de controlos criptográficos para proteção de informação;
- ***Key management*** - Desenvolvimento e implementação de uma política de uso, proteção e tempo de vida de chaves criptográficas.

Os controlos de segurança da Secção 14.2 *Security in development and support processes* são:

- ***Secure development policy*** - Regras para o desenvolvimento de *software* e de sistemas que devem ser estabelecidos e aplicados a desenvolvimentos dentro da organização;
- ***System change control procedures*** - Mudanças para o sistema dentro do tempo de vida do desenvolvimento devem ser controladas pelo uso de processos de controlos de mudanças formais;
- ***Technical review of applications after operating platform changes*** - Quando as plataformas operacionais são alteradas, aplicações criticas para o negócio devem ser revistas e testadas para assegurar que não há nenhum impacto adverso a operações organizacionais ou segurança;
- ***Restrictions on changes to software packages*** - Modificações a *packages* do *software* devem ser desencorajadas, limitadas a mudanças necessárias e todas as alterações devem ser estritamente controladas;
- ***Secure system engineering principles*** - Princípios para a engenharia de sistemas seguros devem ser estabelecidos, documentados, mantidos e aplicados a qualquer esforço de implementação de sistemas de informação;
- ***Secure development environment*** - Organizações devem estabelecer e apropriadamente proteger ambientes de desenvolvimento seguros para o desenvolvimento de sistemas e integração de esforços que cobrem todo o tempo de vida de desenvolvimento do sistema;
- ***Outsourced development*** - A organização deve supervisionar e monitorizar as atividades de sistemas de desenvolvimento *outsourced*;
- ***System security testing*** - Testes das funcionalidades de segurança que devem ser mantidas ao longo do desenvolvimento;
- ***System acceptance testing*** - Testes de aceitação e critérios relacionados devem ser estabelecidos para novos sistemas de informação, *upgrades* e novas versões.

Os controlos de segurança acima enunciados servem para garantir o desenvolvimento de sistemas de *software* mais seguros e garante que a manutenção segura dos mesmos ao longo do seu tempo de vida, sendo que, a sua aplicação torna a execução de um Teste de Intrusão mais complicado devido à manutenção das políticas acima enumeradas.



### 3. SAMM (_Software Assurance Maturity Model_)

O projeto do grupo 8 não de desenvolvimento de software, mas de técnicas de intrusão, 

 Com efeito o projeto escolhido para este exercício é o corrente projeto de Laboratórios de Engenharia Informática - Aplicação de gestão de agenda.
Este projeto tem por objetivo criar uma aplicação para gestão do tempo, onde as atividades de determinado projeto são categorizadas com auxílio de processos de rastreio de uso de aplicações em ambiente desktop e mobile.
Para esse intuito vários dados são recolhidos de forma automática tais como janelas abertas, uso de sistemas de controlo de versão, editores de texto e IDEs, atividades de browser, clientes de email, etc, isto do lado desktop, Ni âmbito do módulo mobile, a ser feito em Android, as informações rastreadas são localizações, registo de chamadas e registo de mensagens.
Os requisitos da aplicação são apenas requisitos de utilizador e os de sistema - funcionais - apenas se focam na usabilidade, disponibilidade, performance, responsividade, manutentabilidade, interoperabilidade, entre outros, sendo que requisitos de utilizador e funcionais de sistema de segurança são na sua maioria ignorados, exceto a existência de um registo e _login_ na aplicação para autenteticação doz utilizadores filtrado por papel funcional no modelo de negócio - gestor de projeto, colaboradores.
Para o desenvolvimento da aplicação existe um repositório privado Gitlab com acesso via VPN para a equipa desktop, enquanto a equipa mobile possui um repositório privado via Github. Os mecanismos de segurança para publicar alterações nos repositórios é via SSH.

#### Pergunta P3.1

- Threat Assessment
- Security Testing
- Environment Hardening

#### Pergunta P3.2

Para todas nível 1

#### Pergunta P3.3

