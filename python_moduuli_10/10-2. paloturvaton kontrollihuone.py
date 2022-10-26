class Hissi:
    def __init__(self, ylink, alink, idhissi):
        self.ylink = ylink
        self.alink = alink
        self.nykyk = alink
        self.idhissi = idhissi

    def siirry_kerrokseen(self, kkerros):
        print(f'Hissi {self.idhissi}')
        if self.ylink >= kkerros >= self.alink:
            if kkerros < self.nykyk:
                while kkerros != self.nykyk:
                    self.kerros_alas()
            elif kkerros > self.nykyk:
                while kkerros != self.nykyk:
                    self.kerros_ylos()
            else:
                print('on jo kyseisessä kerroksessa.')
        else:
            print('kyseistä kerrosta ei ole.')

    def kerros_ylos(self):
        self.nykyk += 1
        print(self.nykyk)

    def kerros_alas(self):
        self.nykyk -= 1
        print(self.nykyk)

class Talo:
    def __init__(self, ylink, alink, hissimaara):
        self.ylink = ylink
        self.alink = alink
        self.hissimaara = hissimaara
        self.hissit = []
        for idhissi in range(1, (hissimaara + 1)):
            self.hissit.append(Hissi(ylink, alink, idhissi))

    def aja_hissia(self, idhissi, kkerros):
        self.hissit[(idhissi - 1)].siirry_kerrokseen(kkerros)

    def palohalyytys(self):
        for hissi in range(self.hissimaara):
            self.hissit[hissi].siirry_kerrokseen(self.alink)


talo1 = Talo(11, 1, 5)


valikko = input('valikko\npoistu hissikontrollihuoneesta (u)\njatka entterillä\n')
while valikko != 'u':
    hissinnumero = int(input('anna hissin numero: '))
    if hissinnumero < 1 or hissinnumero > talo1.hissimaara:
        print('tällaista hissin numeroa ei ole')
    else:
        kohdekerros = int(input('mihin kerrokseen: '))
        talo1.aja_hissia(hissinnumero, kohdekerros)
        valikko = input('\nvalikko\npoistu hissikontrollihuoneesta (u)\njatka entterillä\n')

for hissi in talo1.hissit:
    if hissi.nykyk == hissi.alink:
        print(f'Hissi {hissi.idhissi} on {hissi.nykyk} kerroksessa (pohjakerros).')
    elif hissi.nykyk == hissi.ylink:
        print(f'Hissi {hissi.idhissi} on {hissi.nykyk} kerroksessa (ylin kerros).')
    else:
        print(f'Hissi {hissi.idhissi} on {hissi.nykyk} kerroksessa.')
