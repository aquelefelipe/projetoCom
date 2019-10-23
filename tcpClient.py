
import socket

####ESSE PROGRAMA RODA O CLIENTE; DEVE SER INICIALIZADO APÓS O DNS SERVER E O SERVIDOR.
###Na função, dnsServerComunication(), a variavel nomeDns deve ser setada com o IP da máquina que está rodando o código do dnsServer
### quando for solicitado o site, digite: "fb.com"
###Na função, tcpServerComunication() não é necessária nenhuma modificação;

### faz a comunicação cliente/servidor
def tcpServerComunication(add):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket: ##cria o socket do cliente; o primeiro parametro indica que a rede subjacente está
        #print('add:', add)                                                  ##add = (serverName, serverPort)    

        serverName = add  ## add contain the adress of the server
        serverPort = 12000 ## serverPort is the port od the communication
                                                                            ##usando ipv4 e o sock_stream indica que é uma conexão tcp   
        clientSocket.connect((serverName, serverPort))                      ##essa linha estabele a conexão com o socket servidor
         
        print('\n')                                                           ##por meio do connect é executada a apresentação de 3 vias
        print('---DIGITE A OPÇÃO DESEJADA : -----')
        print('----->ENCERRAR ')
        print('----->LISTAR ')
        print('----->ARQUIVO <nome do arquivo> ')
        print('\n')                                                                
        request = input()         
        while True:
        
            clientSocket.sendall(bytes(request, 'utf-8')) ##VAI MANDAR A FUNÇÃO DESEJADA PRO SERVIDOR
            modifiedSentence= clientSocket.recv(1024)         
        
            if request == "ENCERRAR" :
                print('\n')    
                print(f'Encerrando conexão com Servidor: {add[0]}')
                clientSocket.close()
                break
        
            elif request == "LISTAR":
                print('\n')    
                print("Listando arquivos existentes...")
                print('\n')    
                print(modifiedSentence.decode())
        
            elif request[:7] == "ARQUIVO":
                print('\n')    
                print("Arquivo solicitado: \n")
                print(modifiedSentence.decode())

            else:
                print(modifiedSentence.decode())

            request = input()

#### dnsServerComunication() faz a comunicação cliente/dns ###
def dnsServerComunication():

    nomeDNS = '172.22.67.194' #é o endereço ip da maquina
    portaDNS = 12000

    print('Digite site:')
    message = input(" ")

    sok =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sok.sendto(bytes(message, 'utf-8'), (nomeDNS, portaDNS))

    #dad vai ser o adress do servidorTCP com quem o cliente vai estabelecer conexão
    dad, addr = sok.recvfrom(1024)

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

    tcpServerComunication(end)    ##comunicação com o servidor

###fim da execução cliente

if __name__ == "__main__":
    main()

