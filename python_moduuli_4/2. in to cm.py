while True:
    tuuma = float(input('kerro tuumat: '))
    if tuuma > 0:
        cm = 2.54 * tuuma
        print(cm)
    else:
        break
print('miinus ei toimi :/')
