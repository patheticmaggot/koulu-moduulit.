def summaaja(luku):
    summa = 0
    for n in luku:
        summa += n
    return summa


lista = []

kokonaisluku = input('anna kokonaisluku tai lopeata entterillä: ')

while kokonaisluku != '':
    if (kokonaisluku.strip('-')).isnumeric():
        lista.append(int(kokonaisluku))
        kokonaisluku = input('anna kokonaisluku tai lopeata enterillä: ')
    else:
        print('ei ollut kokonaisluku eikä enter...')
        kokonaisluku = input('anna kokonaisluku tai lopeata enterillä: ')

tulos = summaaja(lista)
print(f'lukujen summa on: {tulos}')
