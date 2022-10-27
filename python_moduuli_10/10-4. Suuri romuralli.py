import random


class Auto:
    def __init__(self, idauto, rekkari, huippunopeus):
        self.idauto = idauto
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


class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            auto.kiihdyta(random.randint(-15, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autolista:
            print(f'\nauto {auto.idauto}: \nrekisteritunnus = {auto.rekkari} \nhuippunopeus = {auto.huippunopeus} '
                  f'\nnykyinen nopeus = {auto.nopeus} \nkuljettu matka = {auto.matka}')

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.matka > self.pituus:
                return True


autolista = []

for k in range(1, 11):
    autolista.append(Auto(k, f'ABC-{k}', random.randint(100, 200)))

kisa1 = Kilpailu('Suuri romuralli', 8000, autolista)

while kisa1.kilpailu_ohi() != True:
    kisa1.tunti_kuluu()
    tuntilaskuri = 0
    if tuntilaskuri % 10 == 0:
        kisa1.tulosta_tilanne()
    kisa1.kilpailu_ohi()
    tuntilaskuri += 1
