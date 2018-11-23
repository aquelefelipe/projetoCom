
import socket, json

serverHost = '172.22.67.194' #cin lua
#serverHost = '192.168.0.13' ##casa de lua
#serverHost = '192.168.0.21'  #FELIPE
serverPort1 = 12000
serverPort2 = 12001
serverPort3 = 12002

dados = []

def addDadosJSON(nome, addr):
        doc = {
                "nome": nome,
                "addr": addr
        }

        dados.append(doc)

##serverCom faz a comunicação DNS/SERVIDOR      
def serverCom():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        sock.bind((serverHost, serverPort1))

        while True: 
                data, addr = sock.recvfrom(1024) 
                print(f'Recebendo dados do SERVIDOR: {addr}')
                addDadosJSON(data.decode(), addr[0])
                #print(dados)
                print('Encerrando conexão com SERVIDOR...')
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


##  clientCom faz a comunicação dns/cliente
def clienteCom():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((serverHost, serverPort2))

        while True:
                data, addr = sock.recvfrom(1024)
                print(f'Cliente  {addr[0]} solicitando: {data.decode()}')
                dominio = searchDomain(data.decode())
                #print(dominio)
                sock.sendto(bytes(dominio, "utf-8"), addr)
                if dominio != "Dominio não encontrado":
                        sock.close()
                        print('Encerrando conexão com cliente...')
                        break
        

## searchDomain procura pelo dominio solicitado pelo cliente
def searchDomain(domain): 
        #print(f'aqui eh dominio: {domain}')
        for x in dados:
                if x["nome"] == domain:
                        return x["addr"]
        return "Dominio não encontrado"

##MAIN
def main():
        print('Iniciando execução do DNS...')

        enderServer = serverCom()
        print('---Nova conexão ---')      
        # clienteCom(enderServer)
        clienteCom()
        print('Encerrando DNS...')

if __name__ == "__main__":
    main()