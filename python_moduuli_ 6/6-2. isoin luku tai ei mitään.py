import random


def nopan_heitto(maksimi):
    noppa = random.randint(1, maksimi)
    return noppa


max1 = int(input('anna nopan suurin luku: '))
tulos = nopan_heitto(max1)
kerrat = 1

while tulos != max1:
    print(tulos)
    kerrat += 1
    tulos = nopan_heitto(max1)

print(tulos)
print(f'heittoja tarvitsit {kerrat} että tulokseksi tuli {max1}.')
