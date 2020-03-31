from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Server started at 127.0.0.1:', serverPort)


def check(number):
    number = int(number)
    counter = 0
    for i in range(1, number):
        if number % i == 0:
            counter = counter + 1
    if counter > 2:
        return 'Numero non primo'
    else:
        return 'Numero primo'


while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')

    print('\nConnection opened\nSocket: ', clientAddress[0], ':', clientAddress[1], '\nMessage: ', message)

    message = str(check(message))
    serverSocket.sendto(message.encode('utf-8'), clientAddress)
