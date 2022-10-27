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


auto1 = Auto('ABC-123', 142)
print(f'auto 1: \nrekisteritunnus = {auto1.rekkari} \nhuippunopeus = {auto1.huippunopeus} '
      f'\nnykyinen nopeus = {auto1.nopeus} \nkuljettu matka = {auto1.matka}\n')


auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f'auton nopeus: {auto1.nopeus} km/h')
auto1.kiihdyta(-200)
print(f'auton nopeus: {auto1.nopeus} km/h')
