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
        self.matka += (self.nopeus * tunnit)

    def tulosta(self):
        print(f'Auton {self.rekkari} kuljettumatka on: {self.matka}')


class Sahkoauto(Auto):
    def __init__(self, rekkari, huippunopeus, kapasiteetti):
        super().__init__(rekkari, huippunopeus)
        self.kapasiteetti = kapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippunopeus, tankin_koko):
        super().__init__(rekkari, huippunopeus)
        self.tankin_koko = tankin_koko


auto1 = Sahkoauto('ABC-15', 180, 52.5)
auto2 = Polttomoottoriauto('ACD-123', 165, 32.3)

auto1.kiihdyta(100)
auto2.kiihdyta(200)

auto1.kulje(3)
auto2.kulje(3)

auto1.tulosta()
auto2.tulosta()
