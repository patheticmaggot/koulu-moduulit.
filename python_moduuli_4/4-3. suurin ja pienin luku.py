maxluku = minluku = luku = input('anna luku: ')

while ((luku.strip('-')).replace('.', '')).isnumeric():
    if float(luku) > float(maxluku):
        maxluku = luku
    elif float(luku) < float(minluku):
        minluku = luku
    luku = input('anna luku: ')

print('isoin numero oli: ' + str(maxluku))
print('pienin numero oli: ' + str(minluku))
