vuosi = int(input('kerro vuosi: '))

if vuosi/100 == int(vuosi/100):
    if vuosi/400 == int(vuosi/400):
        print('vuosi on karkausvuosi')
    else:
        print('vuosi ei ole karkausvuosi')
elif vuosi/4 == int(vuosi/4):
    print('vuosi on karkausvuosi')
else:
    print('vuosi ei ole karkausvuosi')
