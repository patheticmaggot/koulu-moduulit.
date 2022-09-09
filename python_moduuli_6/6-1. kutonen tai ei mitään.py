import random


def nopan_heitto():
    noppa = random.randint(1, 6)
    return noppa


tulos = nopan_heitto()
kerrat = 1

while tulos != 6:
    print(tulos)
    kerrat += 1
    tulos = nopan_heitto()

print(tulos)
print(f'heittoja tarvitsit {kerrat} että tulokseksi tuli 6.')
