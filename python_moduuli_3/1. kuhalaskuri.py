kuhanpituus = float(input('mikä on kuhan pituus senttimetreinä: '))

if kuhanpituus < 37:
    puuttuvamaara = 37-kuhanpituus
    print(f'kuha liian lyhyt ja siitä puuttuu {puuttuvamaara:.4} senttimetriä')
else:
    print('syö kalasi')
