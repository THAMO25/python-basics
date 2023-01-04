# example
value = 0
while value <= 4:
    for num in range(0, 5):
        print(num, end='')
    print()
    value = value + 1
# ex
number = [5, 2, 5, 5, 2]
for stars in number:
    output = ''
    for sum in range(stars):
        output += 'x'
        print(output)

# EXAMPLE
side = int(input('enter the side: '))
left = 0
while left <= 4:
    right = 0
    while right <= 4:
        right = right + 1
        print('*', end='')
    left = left + 1
    print('')