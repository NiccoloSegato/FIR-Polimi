from socket import *

# Creo il welcome socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
binding = ('', serverPort)
serverSocket.bind(binding)

# Il socket ascolta tutte le richieste del client
serverSocket.listen(1)
print('Il server è pronto a ricevere')

while True:
    # Instaurare la connessione con il socket
    connectionSocket, clientAddress = serverSocket.accept()
    print('Connesso con: ', clientAddress)

    # Attendo i messaggi applicativi
    message = connectionSocket.recv(1024)
    message = message.decode('utf-8')
    modifiedMessage = message.upper()

    # Invio la risposta al client
    connectionSocket.send(modifiedMessage.encode('utf-8'))

    # Chiudo la connessione di questo socket
    connectionSocket.close()