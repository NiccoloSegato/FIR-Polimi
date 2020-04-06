from socket import *

# Generalità del Welcome Socket
serverName = 'localhost'
serverPort = 12000

# Apro il socket lato client
clientSocket = socket(AF_INET, SOCK_STREAM)

# Richiedo la connessione
server_address = (serverName, serverPort)
clientSocket.connect(server_address)

# Interazione con l'utente
message = input('Inserisci delle lettere: ')

# Invio del messaggio al server
clientSocket.send(message.encode('utf-8'))

# Ricevo il messaggio dal server
modifiedMessage = clientSocket.recv(1024)
modifiedMessage = modifiedMessage.decode('utf-8')
print('Server message: ', modifiedMessage)

# Chiusura sel socket
clientSocket.close()