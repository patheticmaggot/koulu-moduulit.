import random

numero = (random.randint(1, 10))
arvaus = int(input('arvaa kokonaisluku: '))
arvaukset = 1
while numero != arvaus:
    if arvaus > numero:
        print('Liian suuri arvaus')
    elif arvaus < numero:
        print('Liian pieni arvaus')
    arvaukset += 1
    arvaus = int(input('arvaa uudestaan: '))
print('Onneksi olkoon! Voitit pelin!')
print('arvausten määrä:', arvaukset)
