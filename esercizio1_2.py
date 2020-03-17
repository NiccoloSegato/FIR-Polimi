import requests

def media(list):
    return sum(list)/len(list)

siti = ['http://www.google.com', 'http://www.youtube.com', 'http://www.polimi.it', 'http://www.wikipedia.org', 'http://www.amazon.com', 'http://www.twitter.com']
medie = [] 

for url in siti:
    results = []

    for i in range(10):
        r = requests.get(url)
        print('Test #', i, ' a ', url)
        results.append(r.elapsed.microseconds / 1000)

    medie.append(media(results))

print('Sito con tempo di risposta migliore: ', siti[medie.index(min(medie))])