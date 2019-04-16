







## Pergunta 1.2

__Vulnerabilidades de Projeto__ são defeitos que são inseridos no sistema na fase de planeamento tal como:

- [External Control of File Name or Path](<https://cwe.mitre.org/data/definitions/73.html>) - O sistema permite que o utilizador possa controlar ou influenciar os caminhos ou nomes dos ficheiros que são usados nas operações em *filesystem*. Este tipo de vulnerabilidade resolve-se bastando ter um caminho pré-definido para os ficheiros quando são criados/modificados ou ter um controlo de acesso de modo a impedir utilizadores menos "confiáveis" de obterem acesso a partes restritas da máquina;
- [Argument Injection or Modification](<https://cwe.mitre.org/data/definitions/88.html>) - O software não delimita de modo suficiente os argumentos a serem passados para um componente noutra esfera de controlo, permitindo, assim, que argumentos diferentes sejam dados. Este tipo de vulnerabilidade resolve-se bastando implementar uma verificação de argumentos mais restrita.

**Vulnerabilidades de Codificação** são defeitos que são inseridos no sistema durante a programação do software:

- [Compiler Removal of Code to Clear Buffers](<https://cwe.mitre.org/data/definitions/14.html>) - O compilador, em vez de limpar a memória de acordo com o código *source* acaba por, devido a otimizações, deixar a memória intocada quando não se volta a der da mesma, isto é, "dead store removal". Esta vulnerabilidade resolve-se através de encontrar um "workaround" para o problema sendo que o mesmo ocorre devido a um fator maioritariamente externo ao código;
- [Absolute Path Traversal](<https://cwe.mitre.org/data/definitions/36.html>) - O sistema não verifica se é colocado um *path* num *input* o que pode levar utilizadores a conseguirem acesso a locais previamente restritos. Este tipo de vulnerabilidade resolve-se através da verificação do *input* e se o mesmo contém a estrutura de um caminho.

**Vulnerabilidades Operacionais** são defeitos que são causados pelo ambiente no qual o sistema é executado ou pela sua configuração:

- [Improper Access Control](<https://cwe.mitre.org/data/definitions/284.html>) - O software não restringe, ou restringe incorretamente, o acesso a um recurso por uma pessoa não autorizada. Esta vulnerabilidade pode ser resolvida através da implementação de controlo de acesso ou através de um melhoramento da já existente.
- [Protection Mechanism Failure](<https://cwe.mitre.org/data/definitions/693.html>) - O produto não usa, ou usa incorretamente, mecanismos de proteção que provém defesa suficiente contra ataques diretos contra o produto. Esta vulnerabilidade será difícil de resolver visto que para a implementação de mecanismos de segurança teremos de fazer um teste a fundo no produto de modo a descobrir, ou tentar descobrir, as falhas existentes de modo a serem implementados corretamente.

## Pergunta 1.3

Uma **vulnerabilidade de dia-zero** (*0day vulnerability*) é aquela vulnerabilidade conhecida pelo fabricante do software, porém sem um *patch* de correção disponível. Ou seja, é uma falha de segurança conhecida no software com grande potencial de exploração, uma vez que não existe correção para a mesma.

Por outro lado, uma vulnerabilidade que não seja de dia-zero é uma falha de segurança no software, mas que já foi corrigida pelo fabricante. Nesse caso, só estarão vulneráveis aqueles que estiverem utilizando o software sem a atualização de segurança. Esse é, inclusive, o motivo de se recomendar utilizar os softwares sempre em suas versões mais recentes.

Um exemplo recente de **vulnerabilidade de dia-zero** é a encontrada no navegador Internet Explorer 11. A vulnerabilidade, reportada para a Microsoft no dia 27/03/2019 e sem correção até hoje, necessita apenas que a vítima acesse um ficheiro .MHT especialmente criado. Quando a vítima acessa esse ficheiro, o atacante explora uma falha de injeção de XML (*XML External Entity Injection*) que permite acessar todos os ficheiros do sistema da vítima.

Como a Microsoft ainda não corrigiu a vulnerabilidade, ela continua sendo de dia-zero. Ou seja, **todos os usuários** do Internet Explorer 11 estão vulneráveis a esse ataque e não há praticamente nada que podem fazer para se protegerem (apenas terem bastante atenção aos sites que visitam e ficheiros que abrem no computador).