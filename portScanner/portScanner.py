import socket

def checkIP(ip):
    if (len(target) == 0): return False
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


target = ''
port = ''

while not checkIP(target) or not int(port):
    target = input('Enter IP(Only worked with IP): ')
    port = int(input('Port: '))

print('Scanning', target, 'with port', port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
status = s.connect_ex((target, port))
if(status == 0):
    print('Port', port, 'is opened')
else:
    print('Port', port, 'is closed')
s.close()