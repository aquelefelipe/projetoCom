import socket, glob, json

port = 80 ##pq o dns opera na porta 53
ip = '172.22.67.194' ## é o ip do proprio pc

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((ip, port))

def load_zone():

    jsonzone = {}
    zonefiles = glob.glob('zones/*.zone')
    
    for zone in zonefiles:
        with open(zone) as zonedata:
            data = json.load(zonedata)
            zonename = data["$origin"]
            jsonzone[zonename] = data

    return jsonzone
zonedata = load_zone()

def getflags(flags):

    byte1 = bytes(flags[0:1])
    byte2 = bytes(flags[1:2])

    rflags = ''

    QR = '1'
    OPCODE = ''
    for bit in range(1,5):
        OPCODE += str(ord(byte1)&(1<<bit)) ##pega todos os bits do opcode

    AA = '1'

    TC = '0'

    RD = '0'

    RA = '0'

    Z = '000'

    RCODE = '0000' #RESPONSE CODE

    return int(QR+OPCODE+AA+TC+RD, 2).to_bytes(1,byteorder = 'big')+int(RA+Z+RCODE, 2).to_bytes(1, byteorder = 'big') 

def getquestiondomain(data):
    state = 0
    expectedlenght = 0
    domainstring = ''
    domainparts = []
    x = 0
    y = 0

    for byte in data:
        if state == 1:
            if byte != 0:
                domainstring += chr(byte)
            x += 1
            if x == expectedlenght:
                domainparts.append(domainstring)
                domainstring = ''
                state = 0
                x = 0
            if byte == 0:
                domainparts.append(domainstring)
                break
        else:
            state = 1
            expectedlenght = byte
  
        y += 1 

    questiontype = data[y:y+2]

    # print(domainparts)

    return (domainparts, questiontype) #vai retonar as duas partes do dominio

def getzone(domain):
    global zonedata

    zone_name = '.'.join(domain)
    return zonedata[zone_name]

def getrecs(data):
    domain, questiontype = getquestiondomain(data)
    qt = ''
    if questiontype == b'\x00\x01':
        qt = 'a'

    zone = getzone(domain)

    return (zone[qt], qt, domain)

def buildquestion(domainname, rectype):
    qbytes = b''

    for part in domainname:
        
        length = len(part)
        qbytes += bytes([length])
        
        for char in part:
            qbytes += ord(char).to_bytes(1, byteorder = 'big')

    if rectype == 'a':
        qbytes += (1).to_bytes(2, byteorder = 'big')

    qbytes += (1).to_bytes(1, byteorder = 'big')

    return qbytes

def rectobytes(domainname, rectype, recttl, recval):

    rbytes = b'\xc0\x0c' ##representa a compression order de howcode.org

    if rectype == 'a':
        rbytes = rbytes + bytes([0]) + bytes([1])

    rbytes = rbytes + bytes([0]) + bytes([1])

    rbytes += int(recttl).to_bytes(4, byteorder = 'big')

    if rectype == 'a':
        rbytes = rbytes + bytes([0]) + bytes([4])

        #pra printar a ultima parte: o ipv4 endereço
        for part in recval.split('.'):
            rbytes += bytes([int(part)])

    return rbytes

def buildresponse(data):
    
    #Transaction ID
    TransactionID = data[0:2] 

    #Get the Flags
    Flags = getflags(data[2:4])

    print(Flags)

    #Question Count (num de perguntas q o servidor vai responder... default = 1 )
    QDCOUNT = b'\x00\x01'

    #Aswer Count (vai ser de acordo com quantas respostas o servidor dns vai dar, nesse caso
    # vão ser 3 respostas)
  
    ANCOUNT = len(getrecs(data[12:])[0]).to_bytes(2, byteorder = 'big')
    
    #NameServer Count
    NSCOUNT = (0).to_bytes(2, byteorder = 'big')

    #Additional Count
    ARCOUNT = (0).to_bytes(2, byteorder = 'big')

    dnsheader = TransactionID+Flags+QDCOUNT+ANCOUNT+NSCOUNT+ARCOUNT
    #print(dnsheader) #dá o endereço em hexa

    #construindo DNS body
    dnsbody = b'' 

    #Resposta pra requisição
    records, rectype, domainname = getrecs(data[12:])

    dnsquestion = buildquestion(domainname, rectype)

    for record in records:
        dnsbody += rectobytes(domainname, rectype, record["ttl"], record["value"])

    return dnsheader + dnsquestion + dnsbody


while 1:
    data, addr = sock.recvfrom(512) #
    r = buildresponse(data)
    sock.sendto(r, addr) # vai enviar a resposta r pro addr, nosso end 