import requests
import matplotlib.pyplot as plp

siti = ['https://www.google.com', 'https://www.youtube.com']

medie = []

for url in siti:
    risultati = []

    for i in range(5):
        r = requests.get(url)
        risultati.append(r.elapsed.microseconds / 1000)
    
    medie.append(sum(risultati)/len(risultati))

if medie[0] > medie[1]:
    print('Il primo sito ha un tempo di risposta medio minore')
else:
    print('Il secondo sito ha un tempo di risposta medio minore')