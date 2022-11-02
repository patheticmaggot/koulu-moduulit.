import requests


hakusana = input('anna kaupungin nimi: ')

vastaus = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={hakusana}&APPID=3e7a10de429abd73743b2f470575b9c6&units=metric')
if vastaus.ok:
    print(f'Lämpötila on: {vastaus.json()["main"]["temp"]:.0f}°C')
else:
    print('haku epäonnistui.')