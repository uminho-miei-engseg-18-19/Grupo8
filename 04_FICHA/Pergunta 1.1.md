## Pergunta 1.1
##### Para aceder a alguns sites nos EUA tem que estar localizado nos EUA.
##### 1. Efetuando o comando sudo anonsurf start consegue garantir que está localizado nos EUA?
##### 2.Porquê? Utilize características do protocolo TOR para justificar.

A resposta simples para as perguntas acima é não, o TOR, se for iniciado usando o comando ```sudo anonsurf start```, não irá garantir que o utilizador será visto como estando localizado nos EUA.

O TOR em si tem como objetivo garantir anonimato quando se usa a Internet e serviços anónimos sendo que, para este fim, o TOR irá utilizar Onion Routers (OR) e Onion Proxy's (OP).

O modo geral em que o TOR trabalha consiste em "saltar" de um OR para outro OR através de uma conexão TLS sendo que o OP irá estabelecer os circuitos através da rede e irá também gerar conexões das aplicações ao utilizador. Assim sendo, o IP do utilizador irá estar escondido de pessoas que possam estar a analisar o trafego da rede.

Apesar do dito anteriormente o utilizador poderá alterar o "Exit Node" no ficheiro ```torrc``` alterando ```ExitNodes {}``` para, por exemplo, ```ExitNodes {kr},{ru},{sy},{cn}``` usando os **Tor Country Codes** caso queira garantir qual será a sua localização.