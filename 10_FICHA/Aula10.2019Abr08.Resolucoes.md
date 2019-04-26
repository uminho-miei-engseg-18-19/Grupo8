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

No entanto a aplicação dos mecanismos da fase de requisitos, bem como o suporte a dar aos utilizadores para disponibilização de dados, tanto na fase de codificação, verificação, publicação, de resposta, ou seja, tudo que possa inteferir com a confidencialidade, integridade e disponibilidade dos dados deve ser levado em conta. Por exemplo, é necessário verificar se os requisitos estão implementados de forma correta e se estão de acordo com o que ficou estipulado na fase de requisitos e isto apenas vem nas fases de verificação. De igual modo, na fase de resposta é necessário apoio aos utilizadores e garantir que o sistema continua a cumprir o RGPD.

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

O projeto do grupo 8 não é de desenvolvimento de software, mas de técnicas de intrusão. 

Com efeito o projeto escolhido para este exercício e para poder usar o SAMM a escolha recai para outro projeto é o corrente projeto de Laboratórios de Engenharia Informática - Aplicação de gestão de agenda.

Este projeto tem por objetivo criar uma aplicação para gestão do tempo, onde as atividades de determinado projeto são categorizadas com auxílio de processos de rastreio de uso de aplicações em ambiente desktop e mobile.

Para esse intuito vários dados são recolhidos de forma automática do módulo desktop, tais como janelas abertas, uso de sistemas de controlo de versão, editores de texto e IDEs, atividades de browser, clientes de email, etp.

No âmbito do módulo mobile, a ser feito em Android, as informações rastreadas são localizações, registo de chamadas e registo de mensagens.

Os requisitos da aplicação são apenas requisitos de utilizador e os de sistema - funcionais - apenas se focam na usabilidade, disponibilidade, performance, responsividade, manutentabilidade, interoperabilidade, entre outros, sendo que requisitos de utilizador e funcionais de sistema de segurança são na sua maioria ignorados, exceto a existência de um registo e _login_ na aplicação para autenteticação doz utilizadores filtrado por papel funcional no modelo de negócio - gestor de projeto, 
colaboradores e um administrador. 

Para o desenvolvimento da aplicação existe um repositório privado Gitlab com acesso via VPN para a equipa desktop, enquanto a equipa mobile possui um repositório privado via Github. Os mecanismos de segurança para publicar alterações nos repositórios é via SSH.

#### Pergunta P3.1

Dado as explicações anteriores, os resultados das maturidades nas 12 categorias na _Interview_ foi nulo na sua grande maioria, podendo afirmar que é algo comum em projetos não relacionados diretamente com segurança a nível académico, dado que o foco são as funcionalidades e a segurança é algo para depois. A análise é o mais realista possível do nível de segurança do grupo de trabalho desse projeto - os _stakeholders_ podem ser considerados o coordenador da UC, a organização são o grupo de trabalho e o coordenador e, na menção de projetos no SAMM apenas se refere a este mesmo projeto.

De todas as que foram preenchidas as escolhidas foram as seguintes:
 
- Education & Guidance - 0.10
- Threat Assessment - 0.10
- Security Requiremnts - 0.0 

A escolha recai nestas três dado que as fases de requisitos e modelação do sistema são das mais fundamentais. No entanto, todas as das categorias _Governance_ e _Construction_ precisassem de um SAMM muito bem definido. 

Note-se que não se escolheu nenhuma por causa da maturidade em particular, uma vez que existem algumas com maturidade mais elevada, mas com um objetivo mais estratégico.


#### Pergunta P3.2

Existem 3 níveis de maturidade, sendo que quanto maior o nível, mais tempo e recuros pode levar.

No nível 1 temos abordagens mais reativas e _ad hoc_ como oferecer à equipa recursos para cobrir os tópicos de programação e desenvolvimento seguros. No entanto apenas estamos a oferecer materiais e apenas a um subconjunto da equipa.

No nível 3 as coisas estão mais estruturadas e correm. Inclui educar todo os intervenientes do ciclo de vida do software com mentoria orientada a funções no desenvolvimento seguro. A abordagem é mais activa e trabalha-se com a equipa inteira, como tendo indivíduos reposnsáveis por formar outros e pode-se obter feedback na efetividade dos programas de formação.

Uma vez que na equipa do projeto acima mencionado, apenas 1 elemento da equipa está a receber formação na área de segurança, o sistema é crítico a nível da proteção de dados, formação é o primeiro passo e o mais importante para ter pelo menos a maioria a perceber a importância e perceber o papel da segurança, poder usar melhores práticas em desenvolvimento seguro e ter formação com especialistas na área. Daí que a meta seja o nível 2 para _Education & Guidance_.

Para as restantes o nível desejado é acima de 1, tentando ser mais ambiciosos e ter pelo menos metade da equipa (numa equipa de 5) a considerar riscos de segurança (_Threat Assessment_) e elaborar requisitos de segurança com confiança e documentá-los de forma compreensível com vista um médio prazo. 


Note-se que se planeou tendo em conta a formação anterior e especializações, tempo e outros recursos daí o conservadorismo no planeamento.

Assim temos as seguintes metas ideiais para 4 fases, 3 meses cada, com a inclusão de possibilidade de crescimento na maturidad a médio prazo (após término do projeto da UC).


- Education & Guidance - 2
- Threat Assessment - 1.5
- Security Requiremnts - 1.5

#### Pergunta P3.3

No _Roadmap_ com a estratégia mencionada anteriomente, consegue-se num ano, em 4 fases:

- Education & Guidance - 1.85 
- Threat Assessment - 1.5
- Security Requiremnts - 1.6 

Note-se que na utilização do _toolbox_ conseguimos valores diferentes das metas ideiais. No entanto, depois de usar o _toolbox_ considera-se que se aproximam bastante do ideal para incluir o plano.

As escolhas podem ser vistas na [Folha de cálculo SAMM](Aula10/SAMM_Assessment_Toolbox_v1.5_FINAL.xlsx)

