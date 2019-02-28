
# 1
As empresas escolhidas foram selecionadas através do uso do site https://www.shodan.io/ sendo as mesmas as seguintes:
[OVH SAS](https://github.com/uminho-miei-engseg-18-19/Grupo8/blob/master/03_FICHA/Pergunta%203.1/92.222.93.35.md)

[Iliad-Entreprises](https://github.com/uminho-miei-engseg-18-19/Grupo8/blob/master/03_FICHA/Pergunta%203.1/195.154.134.61.md)

# 2

##### OVH SAS :
OpenSSH Version: 6.7p1 Debian 5+deb8u7

##### Iliad-Entreprises:
OpenSSH Version: 7.4

# 3

Como se pode ver pelas imagens seguintes, consoante a pesquisa feita no site cvedetail a versão com mais vulnerabilidade é a 6.7p1.

![Vulnerabilidades OVH SAS](https://github.com/uminho-miei-engseg-18-19/Grupo8/blob/master/03_FICHA/Pergunta%203.1/2.PNG)

![Vulnerabilidades Iliad-Entreprises](https://github.com/uminho-miei-engseg-18-19/Grupo8/blob/master/03_FICHA/Pergunta%203.1/1.PNG)

# 4

Como as versões do OpenSSH são bastante próximas as vulnerabilidades mais graves nas duas versões são iguais sendo que a versão 6.7p1 tem mais vulnerabilidades.
Se se observar a imagem das "Vulnerabilidades Iliad-Entreprises" encontramos três vulnerabilidades, todas elas com uma avaliação de 5.0 sendo elas, assim, as mais graves.

# 5

Através da leitura da descrição de cada vulnerabilidade chegamos à conclusão que estas vulnerabilidades são graves devido a um atacante poder, por ordem: saber se um certo utilizador existe, fazer enumeração de utilizadores do sistema, conseguir escrever ficheiros vazios. Sendo que existe um exploit conhecido para a 2ª vulnerabilidade.
![Exploit](https://github.com/uminho-miei-engseg-18-19/Grupo8/blob/master/03_FICHA/Pergunta%203.1/4.PNG)