class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'Julkaisu: {self.nimi}')


class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}\n')


class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Päätoimittaja: {self.paatoimittaja}\n')


julkaisu1 = Lehti('Aku Ankka', 'Aki Hyyppä')
julkaisu2 = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)

julkaisu1.tulosta_tiedot()
julkaisu2.tulosta_tiedot()

