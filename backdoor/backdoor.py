import os
import socket
import platform

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


target = ''
port = ''

while not checkIP(target) or not int(port):
    target = input('Enter IP(Only worked with IP): ')
    port = int(input('Port: '))

