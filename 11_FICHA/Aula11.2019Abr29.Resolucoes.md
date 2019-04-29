# Aula TP - 29/Abr/2019

## Exercícios

### 1\. _Buffer Overflow_


#### Pergunta P1.1 - Buffer overflow em várias linguagens

Verifique o que ocorre no mesmo programa escrito em Java (LOverflow2.java), Python (LOverflow2.py) e C++ (LOverflow2.cpp), executando-os.

Explique o comportamento dos programas.


#### Pergunta P1.2 - Buffer overflow em várias linguagens

Verifique o que ocorre no mesmo programa escrito em Java (LOverflow3.java), Python (LOverflow3.py) e C++ (LOverflow3.cpp), executando-os.

Explique o comportamento dos programas.


#### Pergunta P1.3 - Buffer overflow

Analise e teste os programs escritos em C RootExploit.c e 0-simple.c .

+ Indique qual a vulnerabilidade de _Buffer Overflow_ existente e o que tem de fazer (e porquê) para a explorar e (i) obter a confirmação de que lhe foram atribuídas permissões de root/admin, sem utilizar a _password_ correta, (ii) obter a mensagem "YOU WIN!!!".


#### Pergunta P1.4 - Read overflow

Analise e teste o program escrito em C ReadOverflow.c .

+ O que pode concluir?


#### Pergunta P1.5

Agora que já tem experiência em efetuar o _overflow_ a um _buffer_ (cf. pergunta P1.3), consegue fazer o mesmo se for necessário um valor exato?

Compile e execute o programa 1-match.c, e obtenha a mensagem de "Congratulations" no ecrã. Notas:
  + já ouviu falar de _little-endian_ e _big-endian_?

Indique os passos que efetuou para explorar esta vulnerabilidade.

---
---

### 2\. Vulnerabilidade de inteiros


#### Pergunta P2.1

Analise o programa overflow.c.

1. Qual a vulnerabilidade que existe na função _vulneravel()_ e quais os efeitos da mesma?
2. Complete o _main()_ de modo a demonstrar essa vulnerabilidade.
3. Ao executar dá algum erro? Qual?

#### Pergunta P2.2

Analise o programa underflow.c.

1. Qual a vulnerabilidade que existe na função _vulneravel()_ e quais os efeitos da mesma?
2. Complete o _main()_ de modo a demonstrar essa vulnerabilidade.
3. Ao executar dá algum erro? Qual?
