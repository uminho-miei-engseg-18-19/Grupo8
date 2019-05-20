# Aula TP - 06/Mai/2019
## Exercícios

### 1\. _Injection_
#### Pergunta 1.1 - _String SQL Injection_

"SQL Injection" consiste na inserção de código SQL num *input* de modo a conseguir acesso a informação privilegiada sendo utilizado, em certos casos, para fazer *Elevation of Privilege* sendo este ataque possível devido a uma fraca verificação do *input*.

Com a inserção do nome aconselhado ```Smith``` temos o seguinte *output*:

![Normal Input](C:\Users\lilys\Desktop\Universidade\Mestrado\ES\Grupo8\12_FICHA\1.1.1.PNG)

Se colocarmos um *input* que é sempre inerentemente verdadeiro conseguimos ter acesso a toda a informação da base de dados. Neste caso o input escolhido foi ```' OR '1'='1``` visto que a *query* irá colocar a informação recebida entre ```''``` e, deste modo, ficamos com um *input* que será sempre verdade.

![Attack Result](C:\Users\lilys\Desktop\Universidade\Mestrado\ES\Grupo8\12_FICHA\1.1.2.PNG)

#### Pergunta 1.2 - _Numeric SQL Injection_

Com o *input* normal do local, sendo neste exemplo ```Columbia```, temos o seguinte *output*:

![Normal Input](C:\Users\lilys\Desktop\Universidade\Mestrado\ES\Grupo8\12_FICHA\1.2.1.PNG)

Para fazermos o ataque temos de ir ás ferramentas de programador para podermos analisar e editar o HTML. 

Lendo o código inicial verificamos que o valor inserido na *query* do local ```Columbia``` é o ```value = "101"``` conseguindo, assim, editar esse valor de modo a conseguirmos acesso a toda a informação dessa tabela tendo usado o mesmo exemplo que o exercício anterior, ```'' OR '1'='1'```.

![HTML Edit](C:\Users\lilys\Desktop\Universidade\Mestrado\ES\Grupo8\12_FICHA\1.2.2.PNG)

![Attack Result](C:\Users\lilys\Desktop\Universidade\Mestrado\ES\Grupo8\12_FICHA\1.2.3.PNG)

#### Pergunta 1.3 - _Database Backdoors_

---
### 2\. XSS
#### Pergunta 2.1 - _Reflected XSS_

---
### 3\. Quebra na Autenticação
#### Pergunta 3.1 - _Forgot Password_
