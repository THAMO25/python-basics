secret_number = 66

i = 0
while i < 3:
    num = int(input('enter the value: '))
    if secret_number == num:
        print('winner')
        break
    i = i + 1
