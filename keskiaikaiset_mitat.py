luodit = float(input('anna luodit: '))
naulat = float(input('anna naulat: '))
leiviskat = float(input('anna leiviskät: '))

luoti = 13.3
naula = luoti*32
leiviska = naula*20

luoti_paino = luodit*luoti
naula_paino = naulat*naula
leiviska_paino = leiviskat*leiviska
yhteis_paino = luoti_paino+naula_paino+leiviska_paino

yhteis_painokg = int(yhteis_paino/1000)
grammat = yhteis_paino-(yhteis_painokg*1000)

print(yhteis_painokg, f'kiloa ja {grammat:.2f} grammaa.')
