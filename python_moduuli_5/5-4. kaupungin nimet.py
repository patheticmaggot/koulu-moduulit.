varasto = []
kerrat = ['ensimmäinen', 'toinen', 'kolmas', 'toiseksi viimeinen', 'viimeinen']

for k in kerrat:
    kaupungit = input(f'anna {k} kaupungin nimi: ')
    varasto.append(kaupungit)

print('tässä ovat kaupunkiesi nimet järjestyksessä: ')

for i in varasto:
    print(i)
