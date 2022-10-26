class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


auto1 = Auto('ABC-123', 142)

print(f'auto 1: \nrekisteritunnus = {auto1.rekkari} \nhuippunopeus = {auto1.huippunopeus} '
      f'\nnykyinen nopeus = {auto1.nopeus} \nkuljettu matka = {auto1.matka}')
