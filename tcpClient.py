import socket

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

    while True:
        clientSocket.sendall(bytes(input(" "), 'utf-8'))
        modifiedSentence = clientSocket.recv(1024) #quando os caracteres chegam do servidor, eles são colocados na cadeia ModifiedSentence até que a linha termine
        print(f'from Server: ', modifiedSentence.decode())  #printa a sentenca recebida em maiuscula do servidor
        str1 = 'ENCERRAR'
        
        if modifiedSentence.decode() == str1:
            print('Encerrando conexão\n')
            clientSocket.close()  ##encerra a conexao tcp e fecha o socket ela faz o tcp do cliente enviar uma mensagem tcp ao tcp no servidor
            break
    
        elif modifiedSentence.decode() == 'ARQUIVOS' :
            #print (f'Lista de arquivos do servidor: ', modifiedSentence.decode())
            i = 0
            while i<5:
                print('recebendo arquivos:\n') 
                arquivo = clientSocket.recv(1024)
                print (f'Arquivo: \n', arquivo.decode())
                i += 1
            print('Digite proximo comando :')
        
        else: ##Digite qualquer outra coisa
            print('Qual o arquivo que você deseja?')
            clientSocket.sendall(bytes(input(" "), 'utf-8'))
            novoArquivo = clientSocket.recv(1024)
            print (f'Arquivo: ', novoArquivo.decode())

    


######################
#1.criar dns e fazer repositorio
#2.criar lista de arquivos no servidor
#3.fazer as funções do servidor p listar, printar 
#4. função p encerrar conexão no cliente
#alice caimmi - louca

'''perguntas:
1. como vou fazer a requisição pro dns se nosso cliente é tcp
2. preciso fazer dois clientes?
3. como são os arquivos?
4. o dns precisa setar tudo aquilo?
5. AJUDA COM O DNS PLIS'''