import socket

def checkIP(ip):
    if (len(ip) == 0): return False
    ipSplit = ip.split('.')
    if (len(ipSplit) != 4):
        return False
    for value in ipSplit:
        try: 
            value = int(value)
            if(value < 0) or (value > 255):
                return False
        except: return False
    return True

srvAddr = ''
srvPort = ''

while not checkIP(srvAddr) or not int(srvPort):
    srvAddr = input("IP address: ")
    srvPort = int(input("Port: "))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((srvAddr, srvPort))
clientNum = s.listen(1)
print("Server started!")
conn, addr = s.accept()
print("Client information:", addr)

while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(b'Message received!')
    print(data.decode('utf-8'))
conn.close()
