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

# print pattern

row = 5
for i in range(1, row + 1, 1):

    for j in range(1, i + 1):
        print(j, end=' ')

    print("")

# multiplication of 2
n = 2

for i in range(1, 11, 1):
    product = n * i
    print(product)

# div by 5 givn list

num_list = [10, 20, 33, 46, 55]

print('Divisible by 5:')
for num in num_list:
    if num % 5 == 0:
        print(num)

#







