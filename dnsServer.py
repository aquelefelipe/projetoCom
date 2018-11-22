
import socket, json

#serverHost = '172.22.67.194' #LUANA IP
serverHost = '192.168.0.21'  #FELIPE
serverPort = 12000

##TO USANDO O dnsclient.py na pasta documentos pra testar
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((serverHost, serverPort))         ##associamos o num de porta do servidor, serverPort, ao socket                            

while True: 
        #print('Entrei no while')
        data, addr = sock.recvfrom(2048) 
        print(f'Recebendo dados from: {addr}')
        dt = data.decode()
        print(f'cliente mandou: ', dt) 
        break
while True:
        print('Entrei no SEGUNDO while')
        sock =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if dt == 'luana': #to testando com o site = luana, ai só digita luana no cliente
                print('dt == luana')
                message = b"lua123" #seria o endereço do site solicitado
                sock.sendto( message, (serverHost, serverPort))
        break
        
#TA FALTANDO CONFERIR CONFIABILIDADE