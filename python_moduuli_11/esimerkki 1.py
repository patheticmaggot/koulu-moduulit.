class Hahmo:

    def __init__(self, xcoord, ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord

    def siirra(self, xmuutos, ymuutos):
        self.xcoord += xmuutos
        self.ycoord += ymuutos

    def tulosta(self):
        print(f'Keskipisteen koordinaatit: (x:{self.xcoord}, y:{self.ycoord})')


class Ympyra(Hahmo):

    def __init__(self, xcoord, ycoord, sade):
        self.sade = sade
        super().__init__(xcoord, ycoord)

    def skaalaa(self, kerroin):
        self.sade *= kerroin

    def tulosta(self):
        print('\nYmpyrä: ')
        super().tulosta()
        print(f'Säde: {self.sade}')


class Nelio(Hahmo):
    def __init__(self, xcoord, ycoord, sivu):
        self.sivu = sivu
        super().__init__(xcoord, ycoord)

    def skaalaa(self, kerroin):
        self.sivu *= kerroin

    def tulosta(self):
        super().tulosta()
        print('\nNeliö: ')
        # i1 saa arvot -1 ja 1
        for i1 in range(-1, 2, 2):
            # i2 saa arvot -1 ja 1
            for i2 in range(-1, 2, 2):
                print(f'Nurkkapiste: (x:{self.xcoord + i1*self.sivu/2}, y:{self.ycoord +i2*self.sivu/2})')


h1 = Ympyra(200, 140, 25)
h1.siirra(30, -10)
h1.skaalaa(2)
h1.tulosta()

h2 = Nelio(400, 300, 60)
#h2.skaalaa(1.5)
#h2.siirra(-15, 100)
h2.tulosta()
