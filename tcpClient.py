from socket import*

serverName = '172.22.67.194'
serverPort = 12000
##cria o socket do cliente; o primeiro parametro indica que a rede subjacente está
#usando ipv4 e o sock_stream indica que é uma conexão tcp
clientSocket = socket(AF_INET, SOCK_STREAM)
##essa linha estabele a conexão com o socket servidor
#por meio do connect é executada a apresentação de 3 vias
#e uma conexão tcp é estabelecida
clientSocket.connect((serverName,serverPort))

#essa linha obtem uma sentença do usuario, ate que o user digite um enter
sentence = input('Input lowercase sentence: ')

#essa linha envia a cadeia sentence pelo socket do cliente e para a conexão tcp
#
clientSocket.send (sentence)

#quando os caracteres chegam do servidor, eles são colocados na cadeia Modified
#Sentence até que a linha termine
modifiedSentence = clientSocket.recv(4096)
#printa a sentenca recebida em maiuscula do servidor, fechamos o socket do cliente
print (f'from Server {modifiedSentence}')
##encerra a conexao tcp e fecha o socket
##ela faz o tcp do cliente enviar uma mensagem tcp ao tcp no servidor
clientSocket.close()

