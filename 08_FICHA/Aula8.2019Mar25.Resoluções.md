# Aula TP - 25/Mar/2019
## Exercícios
### 1. Blockchain
#### Pergunta 1.1

#### Pergunta 1.2

### 2\. Proof of Work Consensus Model

#### Pergunta 2.1

#### Pergunta 2.2

#### ##### 1

#### ##### 2

Para que um algoritmo de mineração seja adequado, o _miner_ tem que efetuar o puzzle computacionalmente intensivo e ser recompensado por esse trabalho, normalmente na criptomoeda nativa que faz parte do sistema de consenso. Caso contrário, não haveria confiança na criptomoeada dado que utilizadores maliciosos poderiam tentar manipular a criptomoeda. 

Esse puzzle tem que ser difícil de resolver, mas fácil de verificar que a solução é válida, como também todos os nodos conseguem validar quaisquer próximos blocos
propostos e, qualquer próximo bloco que não satisfaça o puzzle
pode ser rejeitado. 

Devido à probabilidade muito baixa de geração bem-sucedida, isso torna imprevisível qual _miner_  na rede será capaz de gerar o próximo bloco.

Para que um bloco seja válido, ele deve ter um valor menor que o destino atual. Isso significa que cada bloco indica que o trabalho é feito gerando-o. Cada bloco contém o _hash_ do bloco anterior. Assim, cada bloco tem uma cadeia de blocos que contém uma quantidade significativa de trabalho.

Mudar um bloco acontece, se se fizer um novo bloco que tem o mesmo antecessor que requer a regeneração de todos os sucessores e refazer o trabalho que eles mantêm. Isso protege a _blockchain_ de adulteração.

Note-se também que, o trabalho envolvido num puzzle não influencia a probalilidade de resolver o puzzle atual ou futuros.

Tendo isto em conta, uma primeira análise ao algoritmo de _proof of work_. Após algumas iterações dá para perceber o padrão descrito na pergunta anterior: todos os números são múltiplos de 9 e a prova anterior divide a prova corrente, sendo que a prova do próximo bloco será o mais próximo múltiplo de 9.

De facto a tabela abaixo dá para mostrar matemáticamente o cálculo de todas as provas, dependendo do índice do bloco, i.e., sendo um índice $k \geq 0$ o índice atual, a prova corrente será $2^{k} \times 3^2 \equiv 2^k \times 9 $ . Este resultado pode ser comprovado para um $k \in [0, \dots , 26]$ na tabela seguinte.


| index | proof-of-work | Cálculo |
| ----- | ------------- | ------- |
|   0   |            9  | $2^0 \times 3^2 $ |
|   1   |           18  | $2^1 \times 3^2 $ |
|   2   |           36  | $2^2 \times 3^2 $ |
|   3   |           72  | $2^3 \times 3^2 $ |
|   4   |          144  | $2^4 \times 3^2 $ |
|   5   |          288  | $2^5 \times 3^2 $ |
|   6   |          576  | $2^6 \times 3^2 $ |
|   7   |         1152  | $2^7 \times 3^2 $ |
|   8   |         2304  | $2^8 \times 3^2 $ |
|   9   |         4608  | $2^9 \times 3^2 $ |
|   10  |         9216  | $2^{10} \times 3^2 $ |
|   11  |        18432  | $2^{11} \times 3^2 $ |
|   12  |        36864  | $2^{12} \times 3^2 $ |
|   13  |        73728  | $2^{13} \times 3^2 $ |
|   14  |       147456  | $2^{14} \times 3^2 $ |
|   15  |       294912  | $2^{15} \times 3^2 $ |
|   16  |       589824  | $2^{16} \times 3^2 $ |
|   17  |      1179648  | $2^{17} \times 3^2 $ |
|   18  |      2359296  | $2^{18} \times 3^2 $ |
|   19  |      4718592  | $2^{19} \times 3^2 $ |
|   20  |      9437184  | $2^{20} \times 3^2 $ |
|   21  |     18874368  | $2^{21} \times 3^2 $ |
|   22  |     37748736  | $2^{22} \times 3^2 $ |
|   23  |     75497472  | $2^{23} \times 3^2 $ |
|   24  |    150994944  | $2^{24} \times 3^2 $ |
|   25  |    301989888  | $2^{25} \times 3^2 $ |
|   26  |    603979776  | $2^{26} \times 3^2 $ |



Ou seja, a primeira razão para o algoritmo não ser válido é a previsibilidade do trabalho futuro e o atual.