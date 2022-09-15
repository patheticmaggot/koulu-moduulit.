nimi = input('anna nimi: ')
nimivarasto = set()

while nimi != '':
    for nimet in nimivarasto:
        if nimi == nimet:
            print('Aiemmin syötetty nimi')
    nimivarasto.add(nimi)
    nimi = input('Uusi nimi: ')
for nimet in nimivarasto:
    print(nimet)
