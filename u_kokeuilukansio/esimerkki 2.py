import requests


hakusana = input('anna TV-sarja nimi: ')


# https://api.tvmaze.com/singlesearch/shows?q=karppi

pyynto = 'https://api.tvmaze.com/singlesearch/shows?q=' + hakusana
# print(pyynto)

vastaus = requests.get(pyynto)
if vastaus.ok:
    #onnistunut pyyntö
    vastaus_json = vastaus.json()
    print(f'löytyi sarja: {vastaus_json["name"]}')
    genret = vastaus_json['genres']
    for g in genret:
        print(f' - kuuluu genreen {g}')
else:
    # epäonnistunut pyyntö
    print('haku epäonnistui.')

