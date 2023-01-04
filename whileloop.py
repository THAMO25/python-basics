# guessing secret number

secret_number = 66

i = 0
while i < 3:
    num = int(input('enter the value: '))
    if secret_number == num:
        print('winner')
        break
    i = i + 1

    # examples
    i = 1
    while i <= 4:
        print('hello welcome')
        i = i + 1

# example for finding 1st 10 even numbers

i = 2
while i <= 20:
    print(i)
    i = i + 2


# example for 1st 10 odd numbers

i = 1
while i < 20:
    print(i)
    i = i + 2

# example for guessing game

secret_num = 9
i = 0
while i < 3:
    num = int(input('enter the number: '))
    if secret_num == num:
        print('winner')
        break
    else:
        print('not a winner')
        i = i + 1

# example

odd_or_even = input('enter odd or even: ')
input_number = int(input('enter the number: '))

i = 0

if odd_or_even == 'even':
    num = 0
    while i < input_number*2:
        i = i + 2
        print(i)
else:
    num = -1
    while i <= input_number:
        num = num + 2
        print(num)
        i = i + 1














