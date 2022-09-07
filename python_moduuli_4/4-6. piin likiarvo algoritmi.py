import math
import random
pisteet = int(input('arvottavien pisteiden määrä: '))
N = 0
n = 0
b = 0

while N < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    N += 1
    if pow(x, 2) + pow(y, 2) < 1:
        n += 1
    else:
        b += 1
print('likiarvosi: ' + str((4*n)/N))
print(f' oikea pii: {math.pi:.6f}')
