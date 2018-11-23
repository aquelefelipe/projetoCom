
import socket

#serverName = '192.168.0.21' #LIPE IP
#serverName = '172.22.67.194' #LUA IP
#serverPort = 12000


### faz a comunicação cliente/servidor
def tcpServerComunication(add):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket: ##cria o socket do cliente; o primeiro parametro indica que a rede subjacente está
        print('add:', add)                                                  ##add = (serverName, serverPort)    

        serverName = add
        serverPort = 12000
                                                                        #usando ipv4 e o sock_stream indica que é uma conexão tcp
        clientSocket.connect((serverName, serverPort))                  ##essa linha estabele a conexão com o socket servidor
                                                                        #por meio do connect é executada a apresentação de 3 vias
        print('---DIGITE A OPÇÃO DESEJADA : -----')
        print('----->ENCERRAR ')
        print('----->LISTAR ')
        print('----->ARQUIVO  ')                                                            
        request = input()         
        while True:
        
            clientSocket.sendall(bytes(request, 'utf-8')) ##VAI MANDAR A FUNÇÃO DESEJADA PRO SERVIDOR
            modifiedSentence= clientSocket.recv(1024)         
        
            if request == "ENCERRAR" :
                print(f'Encerrando conexão com Servidor: {add[0]}')
                clientSocket.close()
                break
        
            elif request == "LISTAR":
                print("Listando arquivos existentes...")
                print(modifiedSentence.decode())
        
            elif request[:7] == "ARQUIVO":
                print("Arquivo solicitado: \n")
                print(modifiedSentence.decode())

            request = input()

#### dnsServerComunication() faz a comunicação cliente/dns
def dnsServerComunication():
    nomeDNS = '192.168.0.21'  #FELIPE
    # nomeDNS = '172.22.67.194' #LUANA
    portaDNS = 12001

    print('Digite site:')
    message = input(" ")

    sok =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sok.sendto(bytes(message, 'utf-8'), (nomeDNS, portaDNS))

    dad, addr = sok.recvfrom(1024)

    print(dad.decode())
    #dad vai ser o adress do servidorTCP
    while True:    
        
        print (f'Endereço do site solicitado: \n', dad.decode())
        print('Encerrando conexão com DNS...')
        break
    sok.close()
    return dad.decode()
        
##MAIN:
###executando cliente
def main():
    print('Iniciando execução...')
    
    end = dnsServerComunication() ##end vai receber o dominio/ip do servidor
    print('o addr tem', end)      ##endereço do tcpServer
    tcpServerComunication(end)    ##comunicação com o servidor

###encerra execução cliente

if __name__ == "__main__":
    main()



        # if modifiedSentence.decode() == "ENCERRAR":
        #     print('Encerrando conexão com Servidor: {addr}\n')
        #     clientSocket.close()                                          ##encerra a conexao tcp e fecha o socket ela faz o tcp do cliente enviar uma mensagem tcp ao tcp no servidor
        #     break
    
        # elif modifiedSentence.decode() == 'ARQUIVOS' :
        #                                                         #print (f'Lista de arquivos do servidor: ', modifiedSentence.decode())
        #     i = 0
        #     while i<5:
        #         print('recebendo arquivos:\n') 
        #         arquivo = clientSocket.recv(1024)
        #         print (f'Arquivo: \n', arquivo.decode())
        #         i += 1
        #     print('Digite proximo comando :')
        
        # elif:                                                   ##Digite qualquer outra coisa
        #     print('Qual o arquivo que você deseja?')
        #     clientSocket.sendall(bytes(input(" "), 'utf-8'))
        #     novoArquivo = clientSocket.recv(1024)
        #     print (f'Arquivo: ', novoArquivo.decode())


