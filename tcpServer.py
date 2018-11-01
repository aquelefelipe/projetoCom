# _*_coding: utf-8 _*_
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort)) ##associamos o num de porta do servidor, serverPort, ao socket
serverSocket.listen(1) ##esse parametro especifica o num de conexoes tcp na fila; e o listen()
#faz com que o servidor escute as requisições tcp do cliente

print ('This server is ready to receive')
while 1:
    ##connectioSocket vai ser um novo socket dedicado a esse cliente especifico
    connectionSocket, addr = serverSocket.accept()
    #o servidor vai enviar sentence como resposta
   # sentence = str(connectionSocket.recv(4096))
   # capitalizedSentence = bytes(sentence.upper())
    sentence = connectionSocket.recv(4096)
    print(sentence)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
##nesse programa, apos ser enviada a sentença modificada, fechamos o socket da conexao
#mas o serverSocket permanece aberto, dai outro cliente pode "bater na porta"
#e enviar uma sentence ao servidor p que seja modificada
    connectionSocket.close()

