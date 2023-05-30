import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-4-30&to=2023-5-23&sortBy=popularity&language=en&apiKey=8def92ec355e40619c79da6aa721e29b')

content = r.json()

print(content['articles'])