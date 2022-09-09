import math


def yksikkohinta(cm, euro):
    ala = math.pi * (cm/200)**2
    yh = euro/ala
    return yh


pizza1koko = float(input('anna ensimmäisen pizzan halkaisija senttimetreinä: '))
pizza1hinta = float(input('anna ensimmäisen pizzan hinta euroina: '))
pizza2koko = float(input('anna toisen pizzan halkaisija senttimetreinä: '))
pizza2hinta = float(input('anna toisen pizzan hinta euroina: '))

pizza1yh = yksikkohinta(pizza1koko, pizza1hinta)
pizza2yh = yksikkohinta(pizza2koko, pizza2hinta)

if pizza1yh < pizza2yh:
    print('ensimmäinen pizza antaa paremman vastineen rahalle.')
elif pizza1yh > pizza2yh:
    print('toinen pizza antaa paremman vastineen rahalle.')
else:
    print('kummastakin pizzasta saa yhtä hyvän vastineen rahalle.')
print(f'ensimmäisen pizzan pyöristetty hinta {pizza1yh:.0f} euroa per neliömetri.')
print(f'toisen pizzan pyöristetty hinta {pizza2yh:.0f} euroa per neliömetri.')
