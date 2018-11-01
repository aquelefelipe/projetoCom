import socket

serverPort = 12000
serverHost = '172.22.67.194'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((serverHost, serverPort)) ##associamos o num de porta do servidor, serverPort, ao socket
    serverSocket.listen(1) ##esse parametro especifica o num de conexoes tcp na fila; e o listen()
    #faz com que o servidor escute as requisições tcp do cliente

    print ('This server is ready to receive')
    while True:
        ##connectioSocket vai ser um novo socket dedicado a esse cliente especifico
        connectionSocket, addr = serverSocket.accept()
        #o servidor vai enviar sentence como resposta
        print('connected by', addr)
        sentence = connectionSocket.recv(1024)
        if not sentence: break
        sentence.decode()
        capitalizedSentence = sentence.upper()
        connectionSocket.sendall(bytes(capitalizedSentence))
##nesse programa, apos ser enviada a sentença modificada, fechamos o socket da conexao
#mas o serverSocket permanece aberto, dai outro cliente pode "bater na porta"
#e enviar uma sentence ao servidor p que seja modificada
        connectionSocket.close()

