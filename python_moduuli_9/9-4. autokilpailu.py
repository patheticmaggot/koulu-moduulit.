import random


class Auto:
    def __init__(self, id, rekkari, huippunopeus):
        self.id = id
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        if (self.nopeus + muutos) <= 0:
            self.nopeus = 0
        elif (self.nopeus + muutos) >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus += muutos

    def kulje(self, tunnit):
        self.matka += (self.nopeus*tunnit)


kilpailijat = []

for k in range(1, 11):
    kilpailijat.append(Auto(k, f'ABC-{k}', random.randint(100, 200)))

km = 0
idn1 = None
while km < 10000:
    for auto in kilpailijat:
        auto.kiihdyta(random.randint(-15, 15))
        auto.kulje(1)
        if auto.matka > km:
            km = auto.matka
            idn1 = auto.id


for n in kilpailijat:
    print(f'\nauto {n.id}: \nrekisteritunnus = {n.rekkari} \nhuippunopeus = {n.huippunopeus} '
          f'\nnykyinen nopeus = {n.nopeus} \nkuljettu matka = {n.matka}')

print(f'\nVoittaja on: auto {idn1}!!!')
