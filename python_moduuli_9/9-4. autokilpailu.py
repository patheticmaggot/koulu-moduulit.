import random


class Auto:
    def __init__(self, ID, rekkari, huippunopeus):
        self.ID = ID
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
IDn1 = None
while km < 10000:
    for auto in kilpailijat:
        auto.kiihdyta(random.randint(-15, 15))
        auto.kulje(1)
        if auto.matka > km:
            km = auto.matka
            IDn1 = auto.ID


for n in kilpailijat:
    print(f'auto {n.ID}: \nrekisteritunnus = {n.rekkari} \nhuippunopeus = {n.huippunopeus} '
          f'\nnykyinen nopeus = {n.nopeus} \nkuljettu matka = {n.matka}')

print(f'\nVoittaja on: auto {IDn1}!!!')
