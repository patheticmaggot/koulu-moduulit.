def parittaja(luku):
    for n in luku:
        if n % 2 == 0:
            paritettulista.append(n)
    return paritettulista


lista = []
paritettulista = []

kokonaisluku = input('anna kokonaisluku tai lopeata entterillä: ')

while kokonaisluku != '':
    if kokonaisluku.strip('-').isnumeric():
        lista.append(int(kokonaisluku))
        kokonaisluku = input('anna kokonaisluku tai lopeata enterillä: ')
    else:
        print('ei ollut kokonaisluku eikä enter...')
        kokonaisluku = input('anna kokonaisluku tai lopeata enterillä: ')

tulos = parittaja(lista)
print(f'tässä parilliset luvut: {tulos}')
