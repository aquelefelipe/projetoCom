
import socket, json

#serverHost = '172.22.67.194' #LUANA IP
serverHost = '192.168.0.21'  #FELIPE
serverPort1 = 12000
serverPort2 = 12001
serverPort3 = 12002

dados = []

##TO USANDO O dnsclient.py na pasta documentos pra testar

def addDadosJSON(nome, addr):
        doc = {
                "nome": nome,
                "addr": addr
        }

        dados.append(doc)

##AGORA FALTA PEGAR O ENDEREÇO DO SERVIDOR
def serverCom():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        sock.bind((serverHost, serverPort1))

        while True: 
                print('Entrei no while servidor')
                data, addr = sock.recvfrom(1024) 
                print(f'Recebendo dados from: {addr}')
                #dt = data.decode()
                #print(f'endereço do servidor: ', dt) 
                # print(f'isso eh dado: {data.decode()}, isso eh endereço: {addr[0]}')
                addDadosJSON(data.decode(), addr[0])
                print(dados)
                sock.close()
                break
        return addr

# def clienteCom(ad):    
#         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#         sock.bind((serverHost, serverPort))         ##associamos o num de porta do servidor, serverPort, ao socket                            

#         while True: 
#                 #print('Entrei no while')
#                 data, addr = sock.recvfrom(1024) 
#                 print(f'Recebendo dados from: {addr}')
#                 dt = data.decode()
#                 print(f'cliente mandou: ', dt) 
#                 break

#         while True:
#                 print('Entrei no SEGUNDO while')
#                 sock =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#                 if dt == 'luana': #to testando com o site = luana, ai só digita luana no cliente
#                         print('dt == luana')
#                         message = str(ad) #seria o endereço do site solicitado
#                         sock.sendto(bytes(message, 'utf-8'), addr)
#                 break
#         sock.close()

def clienteCom():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((serverHost, serverPort2))

        while True:
                data, addr = sock.recvfrom(1024)
                print(f'Dado recebido: {data.decode()}')
                print(f'Endereço origem: {addr[0]}')
                dominio = searchDomain(data.decode())
                print(dominio)
                sock.sendto(bytes(dominio, "utf-8"), addr)
                if dominio != "Dominio não encontrado":
                        sock.close()
                        print('Conexão fechada')
                        break
        
#TA FALTANDO CONFERIR CONFIABILIDADE

def searchDomain(domain):
        print(f'aqui eh dominio: {domain}')
        for x in dados:
                if x["nome"] == domain:
                        return x["addr"]
        return "Dominio não encontrado"

def main():
        print('Iniciando execução do DNS...')

        enderServer = serverCom()
        print('Encerrei comunicação com servidor')
        # clienteCom(enderServer)
        clienteCom()
        print('Encerrando DNS...')

###encerra execução cliente

if __name__ == "__main__":
    main()