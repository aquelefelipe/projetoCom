import socket, json

#####COMENTÁRIOS: ESTE PROGRAMA EXECUTA A FUNÇÃO DO SERVIDOR TCP E DEVE SER INICIALIZADO APÓS O DNS SERVER
#### A variável "serverHost" deve conter o ip da máquina que está rodando o código
#### A variável "nomeDNS" deve conter o ip da máquina que está rodando o código dnsServer.py
####

serverPort = 12000
serverHost = '172.22.67.194' #LUANA

nomes = b''          ## b'' it is for changing the worlds for byte type
response = b''

datas = [ 
                {
                        "nome": "InfraCom",
                        "descricao": "Cadeira do quinto periodo, Professor Jose Suruagy"
                },

                {
                        "nome": "Estatistica",
                        "descricao": "Cadeira do quarto periodo"
                },

                {
                        "nome": "Hardware",
                        "descricao": "Cadeira do terceiro periodo, Professora Edna"
                },

                {
                        "nome": "Software",
                        "descricao": "Cadeira do terceiro periodo, Professor Eduardo"
                },

                {
                        "nome": "IP",
                        "descricao": "Cadeira do primeiro periodo, Professor Alexandre"
                }
]

while True:
        nomeDNS = '172.22.67.194'
        portaDNS = 12000

        print('Comunicando com DNS')
        sok =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        dominio = 'fb.com'
        sok.sendto(bytes(dominio, 'utf-8'), (nomeDNS, portaDNS)) 
        sok.close()
        print('Fechei comunicação com DNSserver')
        sok.close()
        break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket.bind((serverHost, serverPort))         ##associamos o num de porta do servidor, serverPort, ao socket
        serverSocket.listen(3)                              ##esse parametro especifica o num de conexoes tcp na fila; e o listen()
                                                        ##faz com que o servidor escute as requisições tcp do cliente

        print ('--Nova conexão--')
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
                                response = b'Arquivo não encontrado!'
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
        


#FUNÇÕES DO SERVIDOR
# 1. Listar arquivos do servidor CÓDIGO 1
# 2. Sinalizar que arquivo não existe 
# 3. Enviar arquivo para cliente solicitante CÓDIGO 2
# 4. Encerrar conexão

