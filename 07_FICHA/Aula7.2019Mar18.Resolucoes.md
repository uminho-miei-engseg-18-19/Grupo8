# Aula TP - 18/Mar/2019
## Exercícios
### 1. RGPD (Regulamento Geral de Proteção de Dados)

#### Pergunta P1.1 - Direito de ser Informado
A Lei de Proteção de Dados Europeia define que o controlador da informação tem a obrigação de informar, de maneira clara, quais dados serão coletados, bem como:

- A identidade e formas de contato do controlador;
- As bases legais e o propósito do uso da informação;
- As categorias de dados pessoais que serão processados;
- Quais as formas que o dono da informação poderá exercer seus direitos relacionados a seus dados coletados.

Além disso, o RGPD ainda define:

- Se os dados serão transferidos a outros países ou organizações internacionais;
- Por qual período os dados ficarão armazenados;
- Os direitos do dono da informação quanto ao processamento de seus dados pessoais;
- A existência de algum mecanismo automatizado de tomada de decisão;
- O direito de fazer uma reclamação com a autoridade reguladora;
- A existência do direito de retirar o consentimento dado.

Para que um software esteja em conformidade com todas essas exigências, várias técnicas, tecnologias e cuidados precisam ser aplicados no desenvolvimento do software. 

Em primeiro lugar, é necessário que haja, de facto, todo o controle desde a coleta da informação, passando pelo processamento, armazenamento, até sua destruição.

Em cada uma dessas etapas, o controlador da informações precisa garantir não só segurança (para que a informação não seja má utilizada), como também a integridade daquela informção. Antes mesmo da coleta da informação, é preciso adicionar, ao software, um aviso claro com todas as informações necessárias, conforme listado anteriormente. O consentimento, ou a retirada do mesmo, precisam ser respeitados e, para tal, é necessário implementar controles no software para receber essa informação do usuário.

Após dado o consentimento, a coleta dos dados precisa ser feita exatamente na medida em que foi consentida, o que exige a utilização de tecnologias que permitam esse tipo de controle sobre o que é coletado de cada usuário. Conforme os dados são coletados, o software precisa ser programado de tal forma que essa informação não seja visível a terceiros, e que seja armazenada de forma segura. Os desenvolvedores ainda precisam implementar mecanismos capazes de destruir a informação após determinado período, ou quando o consentimento é retirado.

Além disso, é importante que haja uma forma de disponibilizar todos os dados armazenados de um determinado usuário, caso seja solicitado. Por fim, é preciso que haja um setor capaz de atender as demandas dos usuários. Isso exige trabalhadores capacitados e treinados para passarem as informações de maneira clara e correta.

É visível que toda a cadeia de desenvolvimento de software precisa ser adaptada para atender às exigências relacionadas ao direito de ser informado. É necessário treinar e capacitar os desenvolvedores, a equipe de produtos, a equipe comercial, bem como a equipe de suporte.

#### Pergunta P1.2 - ENISA

##### Seção 3 - Proteção de Dados por Padrão na Prática

Essa seção tem como objetivo apresentar os padrões para a proteção de dados na prática. Será utilizado, como base, os critérios definidos pelo Artigo 25 do RGPD (Regulamento Geral de Proteção de Dados). Apesar de os critérios serem tratados de forma separada, ao implementar os controles para proteção de dados na prática, os mesmos deverão ser considerados como um conjunto, uma vez que cada controle terá aspectos de todos os critérios.

###### 3.1 Melhores práticas na proteção de dados por padrão

* **3.1.1 Critério 1: Mínima quantidade de dados pessoas**

  As melhores práticas para cumprir esse critério são:

  * Quanto menos dados, melhor: uma das melhores práticas é coletar apenas os dados estritamente necessários. Para isso, uma boa interface para o usuário é bastante importante, com o intuito de deixar transparente quais são os dados que serão coletados e porque.

  * Coleta granular dos dados com base na necessidade: além de coletar a menor quantidade possível de dados, é importante que essa coleta seja feita de forma granular. Ou seja, ao invés de solicitar todos os dados de uma só vez, as informações serão coletadas de acordo com a necessidade gradual de utilização dos serviços prestados.

  * Utilização de tecnologias que melhoram a privacidade: técnicas criptográficas, de pseudonimização ou anonimização podem ser aplicadas ao dado coletado a fim de que não seja possível relacioná-lo à pessoa de fato.

  * Definir mínimos diferentes para cada propósito: é importante ter bastante claro qual o mínimo de dados necessários para cada cenário. Por exemplo, um aplicativo de mapas precisa ter acesso à localização do telemóvel, mas não necessariamente à lista de contactos; já um aplicativo de mensagens precisa ter acesso à lista de contactos, mas não ao mapa.

* **3.1.2 Critério 2: Mínima extensão do processamento de dados pessoais**

  As principais melhores práticas para esse critério são:
  	

  - Quanto menos processamento, melhor: isso não significa diminuir as operações de processamento, mas sim a quantidade de dados que serão processados.
  - Ferramentas de empoderamento do usuário: possibilitar ao detentor do dado saber e perceber, de forma transparente, o que será feito com seus dados.

* **3.1.3 Critério 3: Mínimo período de armazenamento de dados pessoais**

  As melhores práticas relacionadas ao armazenamento dos dados pessoas são:

  - Quanto menos tempo armazenado, melhor: há casos em que o armazenamento permanente da informação é necessário. Mas na maioria dos casos, o dado não precisa ficar armazenado por muito tempo.

    Nesse critério, nota-se também a importância do uso de ferramentas e técnicas para melhorar a proteção dos dados armazenados (como, por exemplo, ferramentas e políticas de controle de acesso, criptografia, dentre outros).

* **3.1.4 Critério 4: Mínima acessibilidade a dados pessoais**

	- Restringir o acesso de acordo com a necessidade de uso: para tal, usa-se políticas e controles de acesso. Aplica-se, aqui, o princípio *need-to-know*, no qual apenas tem acesso ao dado quem realmente precisa tê-lo.
	- Limitar as formas de compartilhamento: a facilidade na cópia e compartilhamento da informação aumenta a acessiblidade à mesma. Por esse motivo, as técnicas e permissões para essas ações precisam ser revistas e limitadas ao máximo.
	- Não deixar o dado público por padrão, apenas após intervenção ativa: ou seja, por padrão, os dados e informações precisam estar privados ou bastante restritos. Apenas com uma intervenção ativa do dono da informação é que a mesma poderá ser compartilhada e visualizada por mais gente.



#### Pergunta P1.3


**1.** 
   1. Evaluation or scoring
   2. Automated-decision making with legal or similar significant effect
   3. Systematic monitoring
   4. Sensitive data or data of a highly personal nature
   5. Data processed on a large scale
   6. Matching or combining datasets
   7. Data concerning vulnerable data subjects
   8. Innovative use or applying new technological or organisational solutions
   9. Prevents data subjects from exercising a right or using a
       service or a contract

**2.** 

   O projeto escolhido consiste num programa de gestão de agenda, onde todos os dados de utilização do sistema operativo como programas de email, editores de texto, IDE's, git, chamadas, sms e localizações GPS são guardadas para inferir quando é que o utilizador esteve a trabalhar num certo projeto.

   Deste modo iremos satisfazer os critérios:

   * Data processed on a large scale;
   * Data concerning vulnerable data subjects, visto que um menor pode, também, usar o computador que está a ser analisado/monitorizado;
   * Sensitive data or data of a highly personal nature

**3.**  [Template DPIA](URL-GIT)

#### Pergunta P1.4


