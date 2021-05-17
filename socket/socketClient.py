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

def checkExit(message):
    if (message == 'exit()'): return True

srvAddr = ''
srvPort = ''

while not checkIP(srvAddr) or not int(srvPort):
    srvAddr = input("IP address: ")
    srvPort = int(input("Port: "))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Trying connected to", srvAddr)
s.connect((srvAddr, srvPort))
print("Connected to", srvAddr)

while 1:
    message = input('Message to send: ')
    s.sendall(message.encode())
    if (checkExit(message)): break
s.close() 
