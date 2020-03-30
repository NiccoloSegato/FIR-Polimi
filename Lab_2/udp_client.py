from socket import *

serverName = 'localhost' # verrà tradotto dal sistema operatiivo in 172.0.0.1
serverPort = 12001 # numero di porta del processo server, arbittrario ma maggiore di 1023

# Creazione del socket client
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET specifica IPV4 (non 6) e SOCK_DIGRAM indica il collegamento UDP
clientSocket.settimeout(2) # imposto un timeout sulle operazioni del socket

# Specifichiamo la stringa da inviare al server
message = input('Inserisci una stringa: ')

# Invio del messaggio al server
clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort)) #serverName e Port in parentesi perché devono essere UNA TUPLA (non modificabile)

try:
    # risposta del server
    # Viene salvato la risposta nella prima variabile
    # viene salvato l'indirizzo del server nella seconda variabile
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # 2048 = lunghezza buffer, pacchetti più lunghi vengono scartati

    # mostro il messaggio ricevuto
    modifiedMessage =   modifiedMessage.decode('utf-8') # decodifichiamo la risposta
    print('Risposta dal server: ', modifiedMessage) # mostro la risposta
except TimeoutError:
    pass
finally:
    # chiusura della connessione
    clientSocket.close()
