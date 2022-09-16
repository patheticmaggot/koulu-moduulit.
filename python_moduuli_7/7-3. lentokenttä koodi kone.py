valikko = input('haluatko lisätä uuden lentokentän, katsoa vanhempia lisäyksiä vai lopettaa? (uusi, haku, lopeta): ')

lentokentat = {}

while valikko != 'lopeta':
    if valikko == 'uusi':
        uusiicao = input('anna lentokentän ICAO-koodi: ')
        uusinimi = input('anna lentokentän nimi: ')
        lentokentat[uusiicao] = uusinimi
    elif valikko == 'haku':
        icao = input('anna lentokentän ICAO-koodi: ')
        if icao in lentokentat:
            print(f'lentokentän {icao} nimi on {lentokentat[icao]}')
        else:
            print('ICAO-koodia ei ole järjestelmässä.')
    else:
        print('tätä komentoa ei ole järjestelmässä.')
    valikko = input('haluatko lisätä uuden lentokentän, katsoa vanhempia lisäyksiä vai lopettaa? (uusi, haku, lopeta): ')
print('järjestelmä suljettu.')
