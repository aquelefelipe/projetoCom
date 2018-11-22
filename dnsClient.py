
import socket

nome = '172.22.67.194'
#nome = '192.168.0.21'  #FELIPE
porta = 12000
#message = "hello, world!"
print('Digite site desejado:')
message = input(" ")

sok =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sok.sendto(bytes(message, 'utf-8'), (nome,porta)) 
while True:    
    print('Waiting to receive...')
    dado, addr = sok.recvfrom(1024)
    print (f'Endereço de luana: \n', dado.decode())
    #print(f'Recebido do DNS {addr}')
    print('Closing socket...')
    break

'''
serverName = '172.22.67.194'
serverPort = 12000
##cria o socket do cliente; o primeiro parametro indica que a rede subjacente está
#usando ipv4 e o sock_stream indica que é uma conexão tcp
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
##essa linha estabele a conexão com o socket servidor
#por meio do connect é executada a apresentação de 3 vias
#e uma conexão tcp é estabelecida
    clientSocket.connect((serverName,serverPort))
#essa linha obtem uma sentença do usuario, ate que o user digite um enter
#essa linha envia a cadeia sentence pelo socket do cliente e para a conexão tcp

    #while True:
    request = input(" ")
    print(request)
    clientSocket.sendall(bytes(request, 'utf-8'))
    print(request)
    modifiedSentence = clientSocket.recv(1024) #quando os caracteres chegam do servidor, eles são colocados na cadeia ModifiedSentence até que a linha termine
    #print(f'from Server: ', modifiedSentence.decode())  #printa a sentenca recebida em maiuscula do servidor
    #str1 = 'ENCERRAR'
    print(request)
    if request == "ENCERRAR":
    #if modifiedSentence.decode() == request:
        print('Encerrando conexão\n')
        clientSocket.close()  ##encerra a conexao tcp e fecha o socket ela faz o tcp do cliente enviar uma mensagem tcp ao tcp no servidor

    elif request == "LISTAR":
    #elif modifiedSentence.decode() == 'LISTAR' :
        #print (f'Lista de arquivos do servidor: ', modifiedSentence.decode())
        #i = 0
        #while i<5:
        print('recebendo arquivos:\n') 
        #arquivo = clientSocket.recv(1024)
        print (f'Arquivo: \n', modifiedSentence.decode())
            #i += 1
        #print('Digite proximo comando :')
    
    elif request[0:6] == "ARQUIVO": ##Digite qualquer outra coisa
        #print('Qual o arquivo que você deseja?')
        #clientSocket.sendall(bytes(input(" "), 'utf-8'))
        
        #novoDados = clientSocket.recv(1024)
        print (f'Dados: ', modifiedSentence.decode())
'''
