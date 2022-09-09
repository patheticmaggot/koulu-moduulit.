lukujoukko = []

uusiluku = input('anna luku tai lopeata entterillä: ')

while uusiluku.strip('-').isnumeric():
    lukujoukko.append(float(uusiluku))
    uusiluku = input('anna luku tai lopeata enterillä: ')
if uusiluku != '':
    print('ei ollut luku eikä enter...')
    exit()

lukujoukko.sort(reverse=True)

print(lukujoukko[0:5])
