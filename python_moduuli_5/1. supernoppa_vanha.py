import random
tulokset = []
nopat = int(input('monta noppaa haluat heittää: '))

while len(tulokset) < nopat:
    noppa = random.randint(1, 6)
    tulokset.append(noppa)
tulossumma = sum(tulokset)
print(tulokset)
print(tulossumma)
