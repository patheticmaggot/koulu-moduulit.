maxluku = 0
minluku = 0

luku1 = input('laita luku: ')
if luku1.isnumeric():
    print(luku1)
    maxluku = float(luku1)
    minluku = float(luku1)
    while True:
        luku2 = input('laita luku: ')
        if luku2.isnumeric():
            luku2 = float(luku2)
            print(luku2)
            if luku2 >= maxluku:
                maxluku = luku2
            elif luku2 <= minluku:
                minluku = luku2
        else:
            break
print('isoin numero oli: ' + str(maxluku))
print('pienin numero oli: ' + str(minluku))
