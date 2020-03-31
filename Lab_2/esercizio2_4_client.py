from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2)

message = input('Inserisci un numero: ')

try:
    clientSocket.sendto(str(message).encode('utf-8'), (serverName, serverPort))
    response, serverAddress = clientSocket.recvfrom(2048)
    print('Server message: ', response.decode('utf-8'))
except Exception as e:
    print(repr(e))
finally:
    clientSocket.close()