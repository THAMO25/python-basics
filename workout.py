a = 6
b = 7
c = b
b = a
a = c
print(f'a: {a}')
print(f'b: {b}')

patient_name = input('what is your name?: ')
patient_age = input('what is your age?: ')
is_new_patient = input('are you a new patient?yes/no: ')
print(f'we check in a {patient_name}')
print(f'he is {patient_age} years old and is a new pateint')

current_year = 2022
birth_year = int(input('what is your birth year?: '))
current_age = current_year - birth_year
print(f'your age {current_age}')

name = input('what is your name?; ')
favorite_colour = input('what is your favorite colour?: ')
print(f'{name} likes {favorite_colour}')

temp_fahrenheit = float(input('enter the fahrenheit?; '))
temp_cels = (temp_fahrenheit - 32) * 5 / 9
print(f'{temp_cels}')
