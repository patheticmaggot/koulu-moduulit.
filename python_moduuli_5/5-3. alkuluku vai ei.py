kanta = []

alkuluku = int(input('anna koonaisluku: '))

for i in range(2, alkuluku):
    kanta.append(i)
for k in kanta:
    if alkuluku % k == 0:
        print('luku ei ole alkuluku.')
        break
else:
    print('luku on alkuluku')
