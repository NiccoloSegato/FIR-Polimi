# Valutare il tempo di risposta di un server Google

import requests
import matplotlib
import matplotlib.pyplot as plt

r = requests.get('http://www.google.com')

print('Che tipo di variabile è r? -- ', type(r))
print('Che sito abbiamo contattato? -- ', r.url)
print('Qual è lo status code della richiesta? -- ', r.status_code)

# Status Code HTTP:
# 2xx -< Successo
# 4xx -> Client error
# 5xx -> Server error

print('Tempo di risposta: ', r.elapsed.microseconds/1000, 'ms')

# Ripetiamo l'operazione 10 volte per osservare i cambiamenti
# Valutare il tempo di risposta medio, minimo e massimo
statistiche = [] # Lista vuota

for i in range(10):
    r2 = requests.get('http://www.google.com')
    statistiche.append(r2.elapsed.microseconds/1000)

print('Tempo di risposta minore: ', min(statistiche))
print('Tempo di risposta maggiore: ', max(statistiche))
print('Tempo di risposta medio: ', sum(statistiche)/len(statistiche))

# Creazione del grafico delle statistiche
plt.figure()
plt.plot(statistiche)
plt.plot(statistiche, '*') # Evidenzia punti critici
plt.ylim([min(statistiche) * 0.9, max(statistiche) * 1.1])
plt.xlabel('ID Misura')
plt.ylabel('Millisecondi')
plt.title('Test al server http://www.google.com')
plt.grid()
plt.show()





