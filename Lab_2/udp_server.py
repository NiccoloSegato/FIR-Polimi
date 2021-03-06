from socket import *

# definisco il numero della porta, che deve essere uguale a quella specificata nel client
serverPort = 12000

# apro il socket del server
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort)) # imposta la porta, stringa vuota è IP automatico, poi specifico porta

print('Service started at port ', serverPort)

while 1:
    message, clientAddress = serverSocket.recvfrom(2048) #mette il server in attesa di messaggi dal client
    message = message.decode('utf-8')
    print('\nMessage recived')
    print('Client address: ', clientAddress[0], ':', clientAddress[1])
    print('Message: ', message)
    message = message.upper()

    serverSocket.sendto(message.encode('utf-8'), clientAddress)
