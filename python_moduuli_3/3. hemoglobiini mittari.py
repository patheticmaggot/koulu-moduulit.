sukupuoli = input('onko biologinen sukupuolesi nainen vai mies: ')

hemo = int(input('mikä on hemoglobiiniarvosi(g/l)?: '))
min_n = 117
max_n = 175
min_m = 134
max_m = 195

if sukupuoli == 'nainen':
    if hemo < min_n:
        print('hemoglobiinisi on liian alhainen')
    elif hemo > max_n:
        print('hemoglobiinisi on liian korkea')
    else:
        print('hemoglobiinisi on normaali')
else:
    if hemo < min_m:
        print('hemoglobiinisi on liian alhainen')
    elif hemo > max_m:
        print('hemoglobiinisi on liian korkea')
    else:
        print('hemoglobiinisi on normaali.')
