from socket import *

serverAddress = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)

message = input('Inserisci una stringa: ')

try:
    clientSocket.sendto(message.encode('utf-8'), (serverAddress, serverPort))
    response = clientSocket.recvfrom(2048)
    print('Server response: ', response)
except TimeoutError as e:
    print(e.value)
finally:
    clientSocket.close()
