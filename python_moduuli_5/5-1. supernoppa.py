import random

tulokset = []
tulos = 0

nopat = int(input('monta noppaa haluat heittää: '))

while len(tulokset) < nopat:
    noppa = random.randint(1, 6)
    tulokset.append(noppa)

for n in tulokset:
    tulos = tulos + n
print(tulokset)
print(tulos)
