import socket, json

serverPort = 12000

serverHost = '172.22.67.194' #LUANA
#serverHost = '192.168.0.21'  #FELIPE

nomes = b''
response = b''

# datas = [ 
#                 {
#                         "nome": "Luana",
#                         "descricao": "ela eh muito doidona"
#                 },

#                 {
#                         "nome": "Leticia",
#                         "descricao": "ela eh muito doidona tbm"
#                 },

#                 {
#                         "nome": "Felipe",
#                         "descricao": "Ele eh o mais inteligente"
#                 },

#                 {
#                         "nome": "Dudu",
#                         "descricao": "Leticia so pega no pe do coitado"
#                 },

#                 {
#                         "nome": "Renato",
#                         "descricao": "Coitado, namora com Luana"
#                 }
# ]

while True:
        nome = '192.168.0.21'
        porta = 12000

        print('Comunicando com DNS')
        sok =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        message = 'fb.com'
        sok.sendto(bytes(message, 'utf-8'), (nome, porta)) 
        sok.close()
        print('Fechei comunicação com servidor')
        sok.close()
        break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket.bind((serverHost, serverPort))         ##associamos o num de porta do servidor, serverPort, ao socket
        serverSocket.listen(3)                              ##esse parametro especifica o num de conexoes tcp na fila; e o listen()
                                                        ##faz com que o servidor escute as requisições tcp do cliente

        print ('This server is ready to receive')
        while True:
                                                        ##connectioSocket vai ser um novo socket dedicado a esse cliente especifico
                connectionSocket, addr = serverSocket.accept()
                                                        #o servidor vai enviar sentence como resposta
                print(f'connected by', addr)

                while True:
                        sentence = connectionSocket.recv(1024)
                        if not sentence: break        
                        print(sentence.decode()[:7])
                        print(sentence.decode()[8:])
                        #DECODIFICAÇÃO DA SOLICITAÇÃO
                        if sentence.decode() == "LISTAR" :
                                nomes = b''
                                for x in datas:
                                        nomes += bytes(x["nome"], "utf-8")
                                        nomes += b' '
                                connectionSocket.send(nomes)

                        elif sentence.decode()[:7] == "ARQUIVO" :
                                response = b''
                                for x in datas:
                                        if sentence.decode()[8:] == x["nome"] :
                                                response = bytes(x["descricao"], "utf-8")
                                
                                connectionSocket.sendall(response)

                        elif sentence.decode() == "ENCERRAR":
                                connectionSocket.sendall(b'conexao encerrada')
                                print(f'encerrando conexão com cliente {addr}')
                                break
                        else:
                                response = b''
                                response = b'Operacao nao identificada pelo Servidor'
                                connectionSocket.send(response)
        
                connectionSocket.close()
                break
        

##nesse programa, apos ser enviada a sentença modificada, fechamos o socket da conexao
#mas o serverSocket permanece aberto, dai outro cliente pode "bater na porta"
#e enviar uma sentence ao servidor p que seja modificada

#FUNÇÕES DO SERVIDOR
# 1. Listar arquivos do servidor CÓDIGO 1
# 2. Sinalizar que arquivo não existe 
# 3. Enviar arquivo para cliente solicitante CÓDIGO 2

#012345678910
#ENCERRAR
#LISTAR
#ARQUIVO X
