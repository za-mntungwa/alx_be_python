
# print a square pattern of asterisks with the given size

size = int(input('Enter the size of the pattern: '))

while size > 0:
    size_for = size
    for i in range(1, size_for + 1):
        print('*', end='')
    print()
    size -= 1
