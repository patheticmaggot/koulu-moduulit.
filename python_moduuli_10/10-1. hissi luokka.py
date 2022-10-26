class Hissi:
    def __init__(self, ylink, alink):
        self.ylink = ylink
        self.alink = alink
        self.nykyk = alink

    def siirry_kerrokseen(self, kerros):
        if self.ylink >= kerros >= self.alink:
            if kerros < self.nykyk:
                while kerros != self.nykyk:
                    self.kerros_alas()
            elif kerros > self.nykyk:
                while kerros != self.nykyk:
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


h = Hissi(9, 1)

while True:
    anna = int(input('anna kerros: '))
    h.siirry_kerrokseen(anna)
