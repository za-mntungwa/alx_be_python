
# print a square pattern of asterisks with the given size

size = int(input('Enter the size of the pattern: '))

row = 0

while row < size:
    for i in range(1, size + 1):
        print('*', end='')
    print()
    row += 1
