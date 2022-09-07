kayttis = input('käyttäjätunnus: ')
salasana = input('salasana: ')

kayttis_o = 'python'
salasana_o = 'rules'

yritykset = 1

while (kayttis != kayttis_o and salasana != salasana_o) and yritykset < 5:
    yritykset += 1
    kayttis = input('käyttäjätunnus: ')
    salasana = input('salasana: ')
if yritykset < 5:
    print('Tervetuloa')
else:
    print('Pääsy evätty')
