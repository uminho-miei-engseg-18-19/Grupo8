# Aula TP - 11/Fev/2019


## Exercícios


### 1\. Números aleatórios/pseudoaleatórios

#### Pergunta P1.1

Os geradores de números aleatórios podem ser obtidos de fontes de números aleatórios com base em fenómenos físicos estocásticos e imprivisíveis tais como o ruído atmosférico, ruído térmico e outro fenómenos eletromagnéticos e quanticos ou, através de algoritmos computacionais onde a fonte de entropia está na semente do algoritmo.

Os sistemas UNIX-like tem duas fontes de aleatoriedade: o `/dev/random`
e o `/dev/urandom`.
A implementação de ambos usa um geradore que mantém uma estimativa dos bits do ruído do pool de entropia. Desta pool de entropia os números aleatórios são gerados.

No `/dev/random`, quando lido só irá retornar bytes aleatórios dento do número estimado de bits de ruído na pool de entropia. Quando a pool de entropia está vazia, as leituras /dev/random irão bloquear até mais ruído do ambiente a ser obtido.

Por outro lado, o `/dev/urandom` usa uma pool interna para produzir mais bits
pseudo-aleatórias. Ou seja, a leitura não bloqueará, mas o output poderá conter menos entropia

Existem diferentes implementações de algoritmos para gerar sequência pseudo-aleatória:
* Linux 4.8 e mais recentes implementação baseada em ChaCha20
* Outros sistemas Linux-like: Usam o algoritmo de Yarrow, no entanto este foi substituído pelo Fortuna, no entanto é possível que alguns SOs ainda o usem. 

Como já foi dito os algoritmos usam seed obtida no arranque do SO e no shutdown do SO (`/dev/urandom`).  

Note-se que as fontes de aleatoriadade do ambiente para estes dois dispositivos são os tempos entre interrupções, _keystrokes_ do teclado, cliques do rato e outros processos não deterministicos e dificeis de medir.



1. `head -c 32 /dev/random | openssl enc -base64`

2. `head -c 64 /dev/random | openssl enc -base64`

3. `head -c 1024 /dev/random | openssl enc -base64`

4. `head -c 1024 /dev/urandom | openssl enc -base64`

Os pontos 1, 2 e 3 ontêm 32, 64 e 1024 _bytes_ do `/dev/random` que usa o processamento como dito acima. Dado que dependem de eventos que causem entropia, o tempo é demorado e para obter os _bytes_ pedidos o tempo aumenta, ou seja, é necessário esperar que a pool de entropia encha, i.e, bloqueia.

No ponto 4,  como a fonte de aletoriedade é o `/dev/uramdom` é mais rápida, dado que não bloqueia pelos motivos mencionados acima (a _seed_ é que alimentada por eventos do procesamento do sistema) e depois usa um algoritmo para gerar a sequência.

#### Pergunta P1.2

Aqui é pedido que se instale o _haveged_.

No caso da pergunta anterior a entropia é obtida de processos do sistema, muitas vezes causados pelo utilizador e, em sistemas em que não há interação do utilizador, como servidores, isso é um problema. No entanto, a entropia pode ser obtida por hardware, em geradores de números aleatórios em hardware.

- ruído térmico
- efeito fotoelétrico
- outros fenómenos quanticos

O hardware normalmente inclui o uso de um _transducer_ para manter algum aspeto de fenómenos físicos num sinal elétrico, um amplificador para aumentar a amplitude das flutuações de ruído para medilão e um conversor de analógico para digital para converter o output num número digital. Para isto, o Linux providencia  _daemon_ `rndg` para alimentar a entropia nas pools aleatórias.

Todavia, nem sempre é possível ter este tipo de hardware, como também o `rndg` não possuí uma eficiência considerada ótima, dado que é baseado em temporizadores.  De igual modo, pode haver problemas com o hardware, dado que o `rndg` não verifica o seu input é necessário monitorização.

O `haveged` daemon obtêm sequências imprevisíveis de números aleatóriosc om base na entropia de eventos externos baseado no algoritmo HAVEGE. Este usa elementos e processos dos processadores para obter entropia. Os processadores multiescalares  modernos possuem mecanismos para otimizar a performance: vários níves de cache, uso de pipelines, paralelismo ao nível da instrução, etc. Dado que estes componentes não fazem parte da arquitetura do sistema, ou seja, os resultados de uma aplicação normal não dependem desses componentes, como também são voláteis e não podem ser diretamente monitorizados pelo utilizador. Assim, cada invocação ao sistema operativo modifica milhares destes estados binários voláteis.

O `haveged` "semeia" a fonte de aleatoriedade do sistema (`/dev/random`) com estes estados binários. No entanto, não o faz para o `/dev/urandom`.

Executaram-se os comandos:

- `head -c 1024 /dev/random | openssl enc -base64`
- `head -c 1024 /dev/urandom | openssl enc -base64`


Conforme o explicado acima o comando `/dev/random` foi executado com muito mais velocidade. Todavia  o  comando `/dev/urandom` não sofreu alterações praticamente com o mesmo tempo que no exercício anterior.


#### Pergunta P1.3

##### 1

Analisando o código do ficheiro `generateSecret-app.py` notamos que utiliza `shamirsecret.generateSecret(length)` para gerar o segredo a ser utilizado sendo que essa função se encontra no ficheiro shamirsecret do módulo `eVotUM.Cripto`.
Se lermos o seguinte código retirado do ficheiro acima referido podemos inferir que, devido ao uso do `generateRandomData` iremos ter, inicialmente um `s` com tamanho especifico gerado utilizando uma função aleatoria `urandom`.

Utilizando esse `s` temos, então, que iremos eliminar todos os caracteres de s que não contenham letras ascii ou digitos de string.

* `Cripto-4.4.0`

```python
def generateSecret(secretLength):
    """
    This function generates a random string with secretLength characters (ascii_letters and digits).
    Args:
        secretLength (int): number of characters of the string
    Returns:
        Random string with secretLength characters (ascii_letters and digits)
    """
    l = 0
    secret = ""
    while (l < secretLength):
        s = utils.generateRandomData(secretLength - l)
        for c in s:
            if (c in (string.ascii_letters + string.digits) and l < secretLength): # printable character
                l += 1
                secret += c
    return secret

def generateRandomData(length):
    return os.urandom(length)
```
###### 2

Para não ter `s` limitado somente a letras e digitos poderemos alterar o código de modo a que, em vez de retirar todos os elementos que não são "reconheciveis" utilizar o `s` que provem do uso de `generateRandomData` e somente passar esse `s` para Base64 sendo, assim, reconhecido pelo terminal. Ou se quiseremos obter pontuação, por exemplo, acrescentamos `string.punctuation` ou outra propriedade da classe `string`.



### 2\. Partilha/Divisão de segredo (Secret Sharing/Splitting)

#### Pergunta P2.1

##### A

O programa possui uma definição `createSecretComponets` que é a base do _script_. Esta função gera o segredo e divide-o em partes (usando o algoritmo Shamir's Secret Sharing), onde qualquer quorum das partes são suficientes para reconstruir o segredo original.

Para dividir o segredo indicado em 8 partes, determinando um quorum de 5, deve-se primeiro gerar uma chave em format PEM com o comando:

```bash
$ openssl genrsa -aes128 -out mykey.pem 1024
```

Após obter a chave, executar o comando:

```bash
$ python createSharedSecret-app.py 8 5 1 mykey.pem
```

Quando o programa iniciar, primeiro irá solicitar a *passphrase* da chave *mykey.pem*. Em seguida o programa aguarda o *input* do segredo. Neste caso, estamos a utilizar como segredo a frase:

```
Agora temos um segredo extremamente confidencial
```

##### B

Para recuperar o segredo a partir dos componentes gerados, é necessário, em primeiro lugar, gerar o certificado relacionado à chave PEM:

```bash
$ openssl req -key mykey.pem -new -x509 -days 365 -out mykey.crt
```

Há dois programas para recuperar o segredo: `recoverSecretFromComponents-app.py` e `recoverSecretFromAllComponents-app.py`. O primeiro pode ser utilizado para recuperar o segredo com, no mínimo, a quantidade de componentes definida no *quorum*. Já o segundo é utilizado para recuperar o segredo com **todos** os componentes.

Para utilizar o `recoverSecretFromComponents-app.py`, executou-se o comando:

```bash
$ python recoverSecretFromComponents-app.py <5-8> 1 mykey.crt
```

Obs.: há um pequeno bug no código. A função `printUsage()` diz que é necessário passar o `cert.pem` quando o correto seria `cert.crt`.

O número de componentes a ser utilizado precisa estar entre o *quorum* e o total de componentes utilizados ao gerar o segredo (neste caso, entre 5 e 8).

Após executar o comando acima, o programa irá solicitar os componentes. Podem ser informados quaisquer componentes, desde que sejam distintos. Ou seja, não é necessário informar os componentes em alguma ordem específica.

Já para executar o segundo programa, é necessário utilizar o comando:

```bash
$ python recoverSecretFromAllComponents-app.py 8 1 mykey.crt
```

Nesse caso, será sempre necessário fornecer todos os componentes (neste caso 8) para que o programa funcione. Essa funcionalidade pode ser preferível em situações em que se queira ter maior segurança. Por exemplo, para alterar o segredo original, ou para fazer alguma modificação no certificado digital da empresa.


### 3\. Authenticated Encryption
#### Pergunta P3.1

Os requisitos para o produto da empresa são:

* Cifragem (com cifra simétrica) de segredos;
* Decifragem do segredo previamente cifrado;
* O cliente pode decifrar o(s) segredo(s) que cifrou durante o tempo em que pagar a anuidade do serviço;
* Para o cliente identificar o que cifrou, pode etiquetar o segredo;

Além do mais, existe hardware específico de cifra/decifra, em que a chave da cifra é automaticamente mudada todos os dias, tem uma _tag_  "ano.mes.dia". O hardware possibilita HMAC_SHA256 e  possui uma API com:

* `cifra(segredo_texto_limpo)`: retorna `segredo_texto_cifrado`
* `decifra(segredo_texto_cifrado, chave_cifra)`: retorna `segredo_texto_limpo` ou erro
* `hmac(k, str)`: retorna HMAC_SHA256 da `str` e autenticar com a chave secreta `k`.

Em primeiro lugar, é necessário ter em atenção os requisitos da empresa para o serviço. A cifragem tem que ser com uma cifra simétrica e o cliente apenas tem acesso àquilo que cifrou durante um ano e existem metadados (a _tag_ do segredo).

Assim é necessário ter em conta as cifras simétricas mais seguras e ter em conta:

* o custo de quebrar a cifra, excede o valor da informação cifrada;
* o tempo necessário para quebrar a cifra excede o tempo de vida útil da
  informação.

De acordo com a Classificação ENISA duas cifras simétricas possuem estas duas propriedades (AES e Camellia) e a  mesma instituição aconselha o uso de AES-128 para médio prazo e AES-256 para longo prazo. De igual modo, a ENISA diz que o SHA_256 é aconselhado para médio prazo ( usado na API da empresa ) e SHA_512 para longo prazo, no entanto este conselho é de 2014. Por outro lado, o NIST, a ANSSI e BSI, com a avaliações mais recentes, aconselham para médio prazo o AES-128 e o SHA_256, e note-se que o SHA_256 também é aconselhado para longo prazo. O AES-128 também é usado currentemente pela NSA para documentos secretos embora, a NSA esteja a contar com a transição para computação quântica num futuro próximo e também recomenda AES-256 e SHA_256 a contar com essa transição para todos os documentos.

Com efeito, apesar de os dados do cliente poderem estar apenas um ano devido à anuidade, o serviço pode continuar por mais 10 ou 15 anos. Também, dado que são dados pessoais de clientes, cuja confiança está no serviço de critptografia da empresa, é provável que informação muito sensível seja cifrada, ou seja, a informação é valiosa. Por estas razões, recomenda-se o uso de AES-256 para a cifra e SHA-256 para _hashes_.

Para o algoritmo de cifragem autenticada, existem 3 modos (embora existam outros modos como o AES-GCM que possuem autenticação de dados e dados associados):

1. Encrypt-then-MAC;
2. MAC-then-Encrypt;
3. Encrypt-and-MAC;



O `EtM` garante a integridade do texto cifrado, a integridado do texto limpo e que o MAC não providência nenhuma informação sobre o texto limpo (possui IND-CPA, IND-CCA, INT-PTXT e INT-CTXT). O `MtE` não providência integridade do texto cifrado (não é possível saber se um texto cifrado foi modificado ou autentico), no entanto providência integridade do texto limpo e o MAC não providência nenhuma informação sobre o texto limpo (possui IND-CPA, e INT-PTXT). Por último, o `E&M` à semelhança com o `MtE`, não providência integridade do texto cifrado, mas garante a integridado do texto limpo. Todavia, como o MAC é do texto limpo é possível inferir informação do texto limpo a partir do MAC. Note-se que se considerou que o AES-256 é um esquema de cifra não maleável, i.e., não permite transformar um texto cifrado noutro texto cifrado que dê para decifrar o texto limpo (apenas possui INT-PTXT).

Com efeito, o algoritmo de cifragem autenticada recomendado é o Encrypt-then-MAC. Note-se que existem metadados para ser autenticados (a _tag_ de identificação da chave) e a etiqueta que o cliente pode colocar para saber o que cifrou. 



A chave `k` do HMAC deverá ser obtida de uma função da API do HSM, bem como a
chave privada para decifrar o segredo também é obtida do HSM recebendo o
parâmetro data com o formato descrito nos requisitos.

Segue uma possível implementação em pseudo-codigo:

```
function cifra_autenticada(mensagem, etiqueta_mensagem):
    

    segredo_texto_cifrado := cifra(segredo_texto_limpo) + etiqueta_mensagem

    mac := hmac(obter_chave_HSM_HMAC(), segredo_texto_cifrado)

    return segredo_texto_cifrado + mac

```

```
function symmetric_decrypt(segredo_texto_cifrado, etiqueta_mensagem, data):
    
    mensagem_cifrada, mac := segredo_texto_cifrado.split()

    mac2 := hmac(obter_chave_HSM_HMAC(), mensagem_cifrada)

    if mac != mac2 then:
        return erro

    if etiqueta_mensagem existe na bd:
    
        mensagem_cifrada := decifra(segredo_texto_cifrado, obter_chave_privada_HSM(data))

        segredo_texto_limpo, etiqueta_mensagem_2 := mensagem_cifrada.split()

        if etiqueta_mensagem != etiqueta_mensagem_2:
            return erro

    return segredo_texto_limpo
```




### 4\. Algoritmos e tamanhos de chaves
#### Pergunta P4.1

Seguindo o site dado encontramos 7 provedores de certificados confiáveis atualmente sendo que, o especifico para o nosso tema é, somente, o que se encontra relacionado com os cartões de cidadão.

* https://webgate.ec.europa.eu/tl-browser/#/tl/PT/0/0

Seguindo  o site para a divisão  do CEGER (https://webgate.ec.europa.eu/tl-browser/#/tl/PT/0)
encontramos dois certificados, um atual e outro que já não é considerado confiável visto utilizar o algoritmo SHA1 com RSA sendo que o SHA1 já não é considerado seguro visto já se terem encontrado colisões quando se usa o mesmo.

* https://webgate.ec.europa.eu/tl-browser/#/tl/PT/0/1

Analisando o certificado em que ainda se confia chegamos à conclusão que o algoritmo utilizado é a função de hash SHA256 com a cifra RSA sendo a útlima cifra utilizada, também, para a chave pública tendo a mesma um tamanho 2048 bits e com validade até 24 de junho de 2027 às 15:43:57 GMT.

Enquanto isso temos também outros certificados relacionados com o Cartão de cidadão tais como os que se encontram atribuidos pelo Instituto dos Registos e do Notariado I.P. que contém diversos EC's de Assinatura Digital Qualificada do Cartão de Cidadão estando, alguns, já sem utilização.

* **Certificado criado**


```
-----BEGIN CERTIFICATE-----
MIIFQDCCAyigAwIBAgIQW+ApHj8MkelVitA9MDf1STANBgkqhkiG9w0BAQsFADAzMQswCQYDVQQGEwJQVDENMAsGA1UECgwEU0NFRTEVMBMGA1UEAwwMRUNSYWl6RXN0YWRvMB4XDTE1MDYyNDE1NDM1N1oXDTI3MDYyNDE1NDM1N1owQjELMAkGA1UEBhMCUFQxDTALBgNVBAoMBFNDRUUxETAPBgNVBAsMCEVDRXN0YWRvMREwDwYDVQQDDAhFQ0NFIDAwMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMD1nmAQ6iiApqcE9KCvKGTn/3P3WNbrmGguwoUZgDPlNSeopd1ifACygPs0hXSCVbjIEVacsJaQ4jUPAPxGs6/XO2SF49K1M+F02n5QVBDOm7RInu4c5uz6uUp/z0z/51OxBvJT0KCj2aGnLB2vo2atLcyP4pgqeb6lPT3HcTPNTnTnYytAPM2Kj82mJWfMNMop/3qwlaz2SYjvG5ZJNNewGLqOqC++4LYkmNVYaU/r5hX/8p4dlQg+zEP1bQeol8rUQbbtmJ7ZRkD5H01pUngL+1rPE+0V+/qz787ib6jVA513jesBbSxAR9QjMuhdab46q8FBdMqyMPTwqrMYjfcCAwEAAaOCAT8wggE7MA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFOMa2JoMNlrUDiOsDphvgVKeLl0FMB8GA1UdIwQYMBaAFHF/Nd71d3FtHRKc4ZCkuvCpg4+AMA4GA1UdDwEB/wQEAwIBBjA7BgNVHSAENDAyMDAGBFUdIAAwKDAmBggrBgEFBQcCARYaaHR0cDovL3d3dy5lY2VlLmdvdi5wdC9kcGMwZAYIKwYBBQUHAQEEWDBWMCMGCCsGAQUFBzABhhdodHRwOi8vb2NzcC5lY2VlLmdvdi5wdDAvBggrBgEFBQcwAoYjaHR0cDovL3RydXN0LmVjZWUuZ292LnB0L2VjcmFpei5jcnQwNQYDVR0fBC4wLDAqoCigJoYkaHR0cDovL2NybHMuZWNlZS5nb3YucHQvY3Jscy9BUkwuY3JsMA0GCSqGSIb3DQEBCwUAA4ICAQDRjGHFQLgpVdEaDuyC7VwwzRBPqMhhY5mHs84tZL6d1BAUKW6qzLrEB370xEnBgWdxE5dU9jKSZxFeZau9Mkt5Yau3fi2jrYwhacFa+jzeBxthAfVGGD/x9zQU8wCfocrbC7Sfd6t9z7+0drAyAg0A/RwdBjMsrAhHpxxMf5m+5HxlaxY2y5C85ZG0Ru/S4paBDHklK1PNQdPyxrU8QgH/UD6sIz4BgqaSgFijyoaExquCmciX1TSCmxqDHc+c4O6X3iQOB8ZAx2RYsENKJG3DM+thp1yo8mZxEsan1yJcQY4OpKHNvKAq0g9UNyu93ZL/Fn9okVQuFNXp9L9APZsL8p70hAFt2aoThQATaQSRjtb99beGbm5DYvhWh7oli4QnvqmgA/YUrRBz3w0WGCqz+lO0VNXKCKJLPlWwlmeil4YXNbK8Nr+XOvb/XT/yxV09iZBV+hXK/MwQ6dZLbEVwn84WPKiuM3nyQzuEYJHD1iCLy8RM9GM3lNmTL/Wt6mfX66o4+OsR6ZG2PNZxPaPUetZAgX/VCM1T1liL+H7z2aQ7OIjZ1BMo2F27x/QpZSBMIYITZIqxRm0kTEyo90wi14VXlp6scGLcTj6fIE9SD4zOaXKkFg8gc5uzfUtUg2u1fVvqdkywbF1PHgMud9e7scWuX/xLeKCvuTp+Arb78A==
-----END CERTIFICATE-----
```

* **Após execução do comando**:

```
openssl x509 -in ecce.cert -text -noout
```

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            5b:e0:29:1e:3f:0c:91:e9:55:8a:d0:3d:30:37:f5:49
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=PT, O=SCEE, CN=ECRaizEstado
        Validity
            Not Before: Jun 24 15:43:57 2015 GMT
            Not After : Jun 24 15:43:57 2027 GMT
        Subject: C=PT, O=SCEE, OU=ECEstado, CN=ECCE 001
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:c0:f5:9e:60:10:ea:28:80:a6:a7:04:f4:a0:af:
                    28:64:e7:ff:73:f7:58:d6:eb:98:68:2e:c2:85:19:
                    80:33:e5:35:27:a8:a5:dd:62:7c:00:b2:80:fb:34:
                    85:74:82:55:b8:c8:11:56:9c:b0:96:90:e2:35:0f:
                    00:fc:46:b3:af:d7:3b:64:85:e3:d2:b5:33:e1:74:
                    da:7e:50:54:10:ce:9b:b4:48:9e:ee:1c:e6:ec:fa:
                    b9:4a:7f:cf:4c:ff:e7:53:b1:06:f2:53:d0:a0:a3:
                    d9:a1:a7:2c:1d:af:a3:66:ad:2d:cc:8f:e2:98:2a:
                    79:be:a5:3d:3d:c7:71:33:cd:4e:74:e7:63:2b:40:
                    3c:cd:8a:8f:cd:a6:25:67:cc:34:ca:29:ff:7a:b0:
                    95:ac:f6:49:88:ef:1b:96:49:34:d7:b0:18:ba:8e:
                    a8:2f:be:e0:b6:24:98:d5:58:69:4f:eb:e6:15:ff:
                    f2:9e:1d:95:08:3e:cc:43:f5:6d:07:a8:97:ca:d4:
                    41:b6:ed:98:9e:d9:46:40:f9:1f:4d:69:52:78:0b:
                    fb:5a:cf:13:ed:15:fb:fa:b3:ef:ce:e2:6f:a8:d5:
                    03:9d:77:8d:eb:01:6d:2c:40:47:d4:23:32:e8:5d:
                    69:be:3a:ab:c1:41:74:ca:b2:30:f4:f0:aa:b3:18:
                    8d:f7
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:TRUE
            X509v3 Subject Key Identifier: 
                E3:1A:D8:9A:0C:36:5A:D4:0E:23:AC:0E:98:6F:81:52:9E:2E:5D:05
            X509v3 Authority Key Identifier: 
                keyid:71:7F:35:DE:F5:77:71:6D:1D:12:9C:E1:90:A4:BA:F0:A9:83:8F:80

            X509v3 Key Usage: critical
                Certificate Sign, CRL Sign
            X509v3 Certificate Policies: 
                Policy: X509v3 Any Policy
                  CPS: http://www.ecee.gov.pt/dpc

            Authority Information Access: 
                OCSP - URI:http://ocsp.ecee.gov.pt
                CA Issuers - URI:http://trust.ecee.gov.pt/ecraiz.crt

            X509v3 CRL Distribution Points: 

                Full Name:
                  URI:http://crls.ecee.gov.pt/crls/ARL.crl

    Signature Algorithm: sha256WithRSAEncryption
         d1:8c:61:c5:40:b8:29:55:d1:1a:0e:ec:82:ed:5c:30:cd:10:
         4f:a8:c8:61:63:99:87:b3:ce:2d:64:be:9d:d4:10:14:29:6e:
         aa:cc:ba:c4:07:7e:f4:c4:49:c1:81:67:71:13:97:54:f6:32:
         92:67:11:5e:65:ab:bd:32:4b:79:61:ab:b7:7e:2d:a3:ad:8c:
         21:69:c1:5a:fa:3c:de:07:1b:61:01:f5:46:18:3f:f1:f7:34:
         14:f3:00:9f:a1:ca:db:0b:b4:9f:77:ab:7d:cf:bf:b4:76:b0:
         32:02:0d:00:fd:1c:1d:06:33:2c:ac:08:47:a7:1c:4c:7f:99:
         be:e4:7c:65:6b:16:36:cb:90:bc:e5:91:b4:46:ef:d2:e2:96:
         81:0c:79:25:2b:53:cd:41:d3:f2:c6:b5:3c:42:01:ff:50:3e:
         ac:23:3e:01:82:a6:92:80:58:a3:ca:86:84:c6:ab:82:99:c8:
         97:d5:34:82:9b:1a:83:1d:cf:9c:e0:ee:97:de:24:0e:07:c6:
         40:c7:64:58:b0:43:4a:24:6d:c3:33:eb:61:a7:5c:a8:f2:66:
         71:12:c6:a7:d7:22:5c:41:8e:0e:a4:a1:cd:bc:a0:2a:d2:0f:
         54:37:2b:bd:dd:92:ff:16:7f:68:91:54:2e:14:d5:e9:f4:bf:
         40:3d:9b:0b:f2:9e:f4:84:01:6d:d9:aa:13:85:00:13:69:04:
         91:8e:d6:fd:f5:b7:86:6e:6e:43:62:f8:56:87:ba:25:8b:84:
         27:be:a9:a0:03:f6:14:ad:10:73:df:0d:16:18:2a:b3:fa:53:
         b4:54:d5:ca:08:a2:4b:3e:55:b0:96:67:a2:97:86:17:35:b2:
         bc:36:bf:97:3a:f6:ff:5d:3f:f2:c5:5d:3d:89:90:55:fa:15:
         ca:fc:cc:10:e9:d6:4b:6c:45:70:9f:ce:16:3c:a8:ae:33:79:
         f2:43:3b:84:60:91:c3:d6:20:8b:cb:c4:4c:f4:63:37:94:d9:
         93:2f:f5:ad:ea:67:d7:eb:aa:38:f8:eb:11:e9:91:b6:3c:d6:
         71:3d:a3:d4:7a:d6:40:81:7f:d5:08:cd:53:d6:58:8b:f8:7e:
         f3:d9:a4:3b:38:88:d9:d4:13:28:d8:5d:bb:c7:f4:29:65:20:
         4c:21:82:13:64:8a:b1:46:6d:24:4c:4c:a8:f7:4c:22:d7:85:
         57:96:9e:ac:70:62:dc:4e:3e:9f:20:4f:52:0f:8c:ce:69:72:
         a4:16:0f:20:73:9b:b3:7d:4b:54:83:6b:b5:7d:5b:ea:76:4c:
         b0:6c:5d:4f:1e:03:2e:77:d7:bb:b1:c5:ae:5f:fc:4b:78:a0:
         af:b9:3a:7e:02:b6:fb:f0
```