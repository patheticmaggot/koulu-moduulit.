class Hissi:
    def __init__(self, ylink, alink, idhissi):
        self.ylink = ylink
        self.alink = alink
        self.nykyk = alink
        self.idhissi = idhissi

    def siirry_kerrokseen(self, kkerros):
        if self.ylink >= kkerros >= self.alink:
            if kkerros < self.nykyk:
                while kkerros != self.nykyk:
                    self.kerros_alas()
            elif kkerros > self.nykyk:
                while kkerros != self.nykyk:
                    self.kerros_ylos()
            else:
                print('Olet jo kerroksessa.')
        else:
            print('kerros out of range.')

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


talo1 = Talo(11, 1, 5)

for i in talo1.hissit:
    print(i.idhissi, i.ylink, i.alink, i.nykyk)

aloitus = input('tyhjä jatkaa. laita jotain lopettaaksesi: ')
while aloitus == '':
    hissinnumero = int(input('anna hissin numero: '))
    if hissinnumero < 1 or hissinnumero > talo1.hissimaara:
        print('tällaista hissin numeroa ei ole')
    else:
        kohdekerros = int(input('mihin kerrokseen: '))
        talo1.aja_hissia(hissinnumero, kohdekerros)
        aloitus = input('tyhjä jatkaa. laita jotain lopettaaksesi: ')

for i in talo1.hissit:
    print(i.idhissi, i.ylink, i.alink, i.nykyk)