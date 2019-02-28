## SSL Server Test

Realizamos a análise dos sites dos seguintes bancos:

- Banco BPI (https://www.bancobpi.pt)
- Banco Millennium bcp (https://ind.millenniumbcp.pt)
- Caixa Geral de Depósitos (https://www.cgd.pt)

Os dois primeiros (BPI e Millenium) possuem certificados digitais com nota A. Já o último, Caixa Geral de Depósitos, possui nota B. Essa nota é dividida em quatro grandes componentes:

- Certificado
- Protocolos
- Troca de Chave (*Key Exchange*)
- Força da Cifra

### 1. Certificado

Essa componente avalia aspectos do certificado em si, como por exemplo: a entidade certificadora (CA), a data de criação, a data de validade, o algoritmo da assinatura, o tamanho da chave, dentre outras informações.

### 2. Protocolos

Essa componente verifica quais protocolos estão ativos no servidor: SSL 2, SSL 3, TLS 1.0, TLS 1.1, TLS 1.2 e TLS 1.3. Além disso, é feita a verificação de vulnerabilidades e fraquezas dos protocolos suportados pelo servidor.

### 3. Troca de Chave (*Key Exchange*)

São feitos diversos testes simulando diferentes tipos de clientes (Android, Firefox, Internet Explorer, etc). Nesses testes é avaliada a segurança da troca de chaves.

### 4. Força das Cifras

Por fim, o serviço da Qualys analisa as cifras suportadas pelo servidor web. O relatório mostra a ordem das cifras definida pelo servidor, bem como a força das mesmas.

## SSL - Caixa Geral de Depósitos

Como dito anteriormente, a nota da implementação do SSL pelo site da Caixa Geral de Depósitos é B. Essa nota é a derivação das notas para cada uma das quatro componentes descritas acima. É possível ver no relatório, que o certificado obteve nota máxima (100); os protocolos suportados ficaram com nota próxima a 100; já a troca de chaves e a força das cifras obtiveram nota 70 cada uma (o que é considerada uma nota mediana).

![summary-cgd](/home/raphael/Raphael/02_Uminho/ES/Grupo8/tp2/summary-cgd.png)

### Certificado

O certificado obteve nota máxima (100). Vale notar os seguintes aspectos referentes ao certificado:

- Data de validade: o certificado está dentro da validade (31/07/2019)
- Entidade Certificadora (Issuer): DigiCert SHA2 Extended Validation Server CA
- *Revocation status*: certificado não revogado

### Protocolos

Nessa componente, o site obteve nota quase máxima. Vale ressaltar que é muito difícil obter nota máxima nesse ponto, uma vez que quanto menos opções de protocolos o site fornecer, menos clientes conseguirão acessá-lo. Isso ocorre pois cada cliente também possui uma lista de certificados que suporta, e clientes mais antigos (por exemplo, Internet Explorer 7) não possuem suporte a protocolos mais recentes.

No caso do site da Caixa Geral de Depósitos, são suportados os protocolos TLS da versão 1.0 até a versão 1.2. Apesar da alta nota, importa notar que o TLS versão 1.0 já não é mais considerado seguro, e é aconselhável sua desativação.

### Troca de Chaves

#### Perfect Forward Secrecy (PFS)

O *Perferct Forward Secrecy* é uma funcionalidade presente em alguns algoritmos de acordo/troca de chaves. Com o PFS, será gerada uma chave para cada sessão de comunicação. Isso garante que o comprometimento da chave privada de uma sessão não tenha impacto em outras comunicações do servidor.

De acordo com a empresa que fornece o *SSL test* (Qualys), a utilização de um protocolo de troca de chaves que não suporte o *Perfect Forward Secrecy* fará com que a nota do site seja rebaixada automaticamente para B. No caso do site da Caixa Geral de Depósitos, é exatamente o que acontece. Conforme publicação da própria Qualys, a utilização do RSA por si só não garante o PFS. Recomenda-se o suporte ao algoritmo ECDHE (*Elliptic-curve Diffie-Hellman Exchange*).

### Força das Cifras

#### Authenticated Encryption with Associated Data (AEAD)

Cifras AEAD possuem a característica de garantir os três pilares da segurança (confidencialidade, integridade e autenticidade) simultaneamente. Conforme a Qualys, esse é a única abordagem criptográfica realmente segura para ser utilizada no SSL/TLS.

O site da Caixa Geral de Depósitos, nas três versões do protocolo TLS suportadas, utiliza AES com CBC (modo conhecidamente inseguro). Da mesma forma como acontece na ausência do PFS, a ausência do AEAD faz com que a nota seja rebaixada automaticamente para B.

Para ambos os casos (ausência de PFS e AEAD), é possível ver as falhas na tabela abaixo:

![1551115275818](/home/raphael/Raphael/02_Uminho/ES/Grupo8/tp2/1551115275818.png)

O modo criptográfico CBC (*Cipher Block Chaining*) é vulnerável a ataques do tipo *timing attack*, que permite descriptografar os dados e lê-los em texto claro.



## *Downgrade Attack*

### Como funciona

O *downgrade attack* é utilizado, na maioria das vezes, em conjunto com o ataque de *ARP Poisoning* para realizar um *Man-in-the-Middle* em comunicações via SSL/TLS. O ataque funciona da seguinte forma:

- O atacante realiza, de dentro da rede interna, um *ARP Poisoning*, que força as comunicações entre certos clientes da rede passarem pela sua máquina;
- A partir de então, é feito o *downgrade attack* para o servidor utilizar um protocolo inseguro (por exemplo, SSL v3) na comunicação SSL/TLS com aquele cliente;
- Por fim, o atacante realiza a quebra da criptografia desse procolo inseguro e consegue ler toda a comuniação entre o cliente e o servidor.

Para o *downgrade attack* funcionar, o atacante deve simular um cliente com suporte apenas ao protocolo fraco. Se o servidor estiver mal configurado, ele irá aceitar essa comunicação e a mesma se dará através desse meio inseguro.

### Prevenção

Para prevenir esse tipo de ataque, o servidor deve ser propriamente configurado. O servidor não pode aceitar se comunicar com o client através de protocolos inseguros (como o SSL e o TLS 1.0). Como já foi visto anteriormente, isso pode acarretar na perda de clientes - pois nem todos suportam versões mais recentes do TLS.

Uma outra forma de mitigar esse risco está no uso de navegadores que previnem o ataque do lado do cliente. Alguns navegadores já não aceitam fechar conexões com protocolos inseguros. O uso de navegadores mais seguros precisa fazer parte da política de segurança da empresa.

### Referências

Qualys' Blog: https://blog.qualys.com/ssllabs/2018/02/02/forward-secrecy-authenticated-encryption-and-robot-grading-update

Scott Helme's Blog: https://scotthelme.co.uk/perfect-forward-secrecy/

GlobalSign's Blog: https://www.globalsign.com/en/blog/disable-tls-10-and-all-ssl-versions/

RFC 7507: https://tools.ietf.org/html/rfc7507