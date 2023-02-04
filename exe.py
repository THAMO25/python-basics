# square pattern input form user
num = int(input('enter the no: '))
for i in range(num):
    for j in range(num):
        print('*', end='')
    print('')
# sqaure pattern
num = 5
for i in range(0, num):
    for j in range(0, num):
        print('*', end='')
    print('')

# hollow squre pattern input from user
num = int(input('enter the number: '))
for i in range(num):
    for j in range(num):
        if i == 0 or i == num - 1 or j == 0 or j == num - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# hollow square pattern
num = 4
for i in range(0, num):
    for j in range(0, num):
        if i == 0 or i == num - 1 or j == 0 or j == num - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# right angle triangle
num = int(input('enter the number:'))
for i in range(num):
    for j in range(i + 1):
        print("*", end='')
    print()

#left angle triangle
num = int(input('enter the number: '))
for i in range(num):
    for j in range(num - i - 1):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()

#reverse left triangle
num = int(input('enter the number: '))
for i in range(num):
    for j in range(i):
        print(' ', end='')
    for j in range(num - i):
        print('*', end='')
    print()

#reverse right triangle
num = int(input('enter the number:'))
for i in range(num):
    for j in range(num - i):
        print('*', end='')
    print()

#number pattern right triangle
num = int(input('enter the number:'))
for i in range(num):
    for j in range(i + 1):
        print(j+1, end='')
    print()

# palindrome using range
palyn = input('enter the string:')
rev_palyn = palyn[::-1]
if palyn == rev_palyn:
    print('it is a palyndrome')
else:
    print('it is not a palyndrome')

#add a number recursively
input = 5
output = 0
while (input > 0):
    output = output + input
    input = input - 1
print(output)

#reverse the string
name = input('enter the name: ')
output = ''
i = len(name) - 1
while (i >= 0):
    output = output + name[i]
    i = i - 1
print(output)

# finding greatest of three numbers
num1 = float(input('enter the first number: '))
num2 = float(input('enter the second number:'))
num3 = float(input('enter the third number:'))
if num1 >= num2 and num1 >= num3:
    print('num1 is greatest')
if num2 >= num1 and num2 >= num3:
    print('num2 is greatest')
if num3 >= num1 and num3 >= num2:
    print('num3 is greatest')

#armstrong number
num = int(input('enter the number: '))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10
if num == sum:
    print('the number is amstrong')
else:
    print('the number is not an amstrong')

#replce a string space with character
sen = input('enter the sentence: ')
full_sen = ''
new_ch = input('enter the character: ')
for i in sen:
    if i == ' ':
        i = new_ch
    full_sen = full_sen + i
print('the sentence is:', full_sen)


sen = input("Enter the sen : ")
result = ''
for i in sen:
    if i in ('a', 'e', 'i', 'o', 'u'):
        i=''
    result=result+i
print(result)










