numero = int(input('kerro kuukauden numero (1-12): '))
vuodenajat = ('talvi', 'kevät', 'kesä', 'syksy')
if numero in (1, 2, 12):
    print(vuodenajat[0])
elif numero in (3, 4, 5):
    print(vuodenajat[1])
elif numero in (6, 7, 8):
    print(vuodenajat[2])
elif numero in (9, 10, 11):
    print(vuodenajat[3])
else:
    print('numero ei ole kuukauden numero.')
