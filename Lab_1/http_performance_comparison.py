# Paragonare i tempi di risposta di più server HTTP
import requests
import matplotlib.pyplot as plt

siti = ['http://www.gazzetta.it', 'http://www.netflix.it', 'http://www.netflix.com/it-en/', 'http://www.apple.com/it/']

plt.figure()

for url in siti:
    print('Testing ', url)
    statistiche = []

    for i in range(10):
        r = requests.get(url)
        statistiche.append(r.elapsed.microseconds/1000)

    print('Tempo di risposta MINIMO: ', min(statistiche))
    print('Tempo di risposta MASSIMO: ', max(statistiche))
    print('Tempo di risposta MEDIO: ', sum(statistiche)/len(statistiche))

    plt.plot(statistiche, label=url)

plt.ylim([0, 1000])
plt.xlabel('ID Misura')
plt.ylabel('Millisecondi')
plt.title('Test su siti diversi')

plt.legend(loc='lower right')
plt.grid()

plt.show()
