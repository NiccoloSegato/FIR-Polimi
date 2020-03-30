from socket import *

# definisco il numero della porta, che deve essere uguale a quella specificata nel client
serverPort = 12000

# apro il socket del server
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort)) # imposta la porta, stringa vuota è IP automatico, poi specifico porta

print('Service started at port ', serverPort)
