print('Star Pattern')
for row in range (1,6):
    for stars in range(row):
        print("*", end="")
    print('\n')

print('Reverse star Pattern')
for row in range(6,1,-1):
    for stars in range(row):
        print("*", end="")
    print('\n')

