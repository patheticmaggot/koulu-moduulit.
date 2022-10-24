import random


class Auto:
    def __init__(self, rekkari, huippunopeus):
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

auto(k) = Auto(f'ABC-{k}', hn)

for k in range(1, 11):
    hn = random.randint(100, 200)
    kilpailijat.extend([autok = Auto(f'ABC-{k}', hn)])



for k in kilpailijat:
    print(k)

