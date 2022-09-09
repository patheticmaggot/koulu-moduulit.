def muuntaja(gallon):
    litra = gallon*3.785
    return litra


gallonit = float(input('anna gallonit: '))

while gallonit > 0:
    tulos = muuntaja(gallonit)
    print(f'on litroina: {tulos:.3f}')
    gallonit = float(input('anna gallonit: '))
print('miinus on rikki :/')
