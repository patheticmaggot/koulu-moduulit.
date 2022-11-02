import requests


vastaus = requests.get('https://api.chucknorris.io/jokes/random')

if vastaus.ok:
    print(vastaus.json()['value'])
else:
    print('haku epäonnistui.')
