import requests


# 3e7a10de429abd73743b2f470575b9c6
# https://api.openweathermap.org/data/2.5/weather?q=espoo&APPID=3e7a10de429abd73743b2f470575b9c6

hakusana = input('anna kaupungin nimi: ')

pyynto = f'https://api.openweathermap.org/data/2.5/weather?q={hakusana}&APPID=3e7a10de429abd73743b2f470575b9c6'


vastaus = requests.get(pyynto)
if vastaus.status_code == 200:
    #onnistunut pyyntö
    vastaus_json = vastaus.json()
    print(f'löytyi kaupunki: {vastaus_json["name"]}')
    genret = vastaus_json['main']['temp']
    for g in genret:
        print(f' sää on: {g}')
else:
    # epäonnistunut pyyntö
    print('haku epäonnistui.')
