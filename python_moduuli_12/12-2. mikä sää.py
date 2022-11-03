import requests


hakusana = input('anna kaupungin nimi: ')
apikey = '3e7a10de429abd73743b2f470575b9c6'
units = 'metric'
language = 'FI'

para = {'appid': apikey, 'units': units, 'lang': language, 'q': hakusana}

vastaus = requests.get(f'https://api.openweathermap.org/data/2.5/weather', para)

if vastaus.ok:
    print(f'Säätila: {vastaus.json()["weather"][0]["description"]}')
    print(f'Lämpötila: {vastaus.json()["main"]["temp"]:.0f}°C')
else:
    print('haku epäonnistui.')
