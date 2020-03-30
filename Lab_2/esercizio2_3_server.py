from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print('Service started at localhost:', serverPort)

def findCaps(message):
    return message.upper()

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')

    print('\nConnection opened\nSocket: ', clientAddress[0], ':', clientAddress[1], '\nMessage: ', message)
    message = findCaps(message)

    serverSocket.sendto(message.encode('utf-8'), clientAddress)



