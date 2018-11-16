
import socket, json

serverPort = 12000
serverHost = '172.22.67.194'

nomes = b''

datas = [ 
                {
                        "nome": "Luana",
                        "descricao": "ela eh muito doidona"
                },

                {
                        "nome": "Leticia",
                        "descricao": "ela eh muito doidona tbm"
                },

                {
                        "nome": "Felipe",
                        "descricao": "Ele eh o mais inteligente"
                },

                {
                        "nome": "Dudu",
                        "descricao": "Leticia so pega no pé do coitado"
                },

                {
                        "nome": "Renato",
                        "descricao": "Coitado, namora com Luana"
                }
]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((serverHost, serverPort))         ##associamos o num de porta do servidor, serverPort, ao socket
    serverSocket.listen(1)                              ##esse parametro especifica o num de conexoes tcp na fila; e o listen()
                                                        ##faz com que o servidor escute as requisições tcp do cliente

    print ('This server is ready to receive')
    while True:
                                                        ##connectioSocket vai ser um novo socket dedicado a esse cliente especifico
        connectionSocket, addr = serverSocket.accept()
                                                        #o servidor vai enviar sentence como resposta
        print('connected by', addr)
        sentence = connectionSocket.recv(1024)
        if not sentence: break        
        #sentence.decode()
        
        #DECODIFICAÇÃO DA SOLICITAÇÃO
        if sentence.decode() == "LISTAR" :
                for x in datas:
                        nomes += bytes(x["nome"], "utf-8")
                        nomes += b' '
                connectionSocket.sendall(nomes)

        elif sentence.decode()[0:6] == "ARQUIVO" :
                for x in datas:
                        if sentence.decode()[8:] == x["nome"] :
                                connectionSocket.sendall(bytes(x["descricao"], "utf-8"))

        elif sentence.decode() == "ENCERRAR":
                connectionSocket.sendall(b'conexao encerrada')
                connectionSocket.close()
                print("encerrando conexão com cliente ${addr}", addr)
                break


        

##nesse programa, apos ser enviada a sentença modificada, fechamos o socket da conexao
#mas o serverSocket permanece aberto, dai outro cliente pode "bater na porta"
#e enviar uma sentence ao servidor p que seja modificada


#FUNÇÕES DO SERVIDOR
# 1. Listar arquivos do servidor CÓDIGO 1
# 2. Sinalizar que arquivo não existe 
# 3. Enviar arquivo para cliente solicitante CÓDIGO 2
