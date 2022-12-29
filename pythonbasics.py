# below is the example for print the string in python

print('hello world')

print(' ||||')

# python will consider the below statement as expression, string(*) to be printed 10 times
# expression is a piece of code that produce the value

print('*' * 10)

# swap a variable example a=5,b=6

a = 5
b = 6
print(f'value of a before swap: {a}')
print(f'value of b before swap: {b}')
c = b
b = a
a = c
print('after swap')
print(f'a: {a}')
print(f'b: {b}')

# exercise 2 ;
name = 'john smith'
age = 20
is_new = True

patient_name = input('what is your name: ')
patient_age = input('what is your age: ')
is_patient_new = input('are you a new patient: True/False')
print(f'we check in a patient named {patient_name}. ')
print(f'he is {patient_age} years old and is a new patient. ')

# exercise 3
person_name = input('what is your name? ')
favourite_colour = input('what is your favourite colour? ')
print(f'"{person_name} likes {favourite_colour}"')

# exercise4 below i
current_year = 2022
birth_year = input('what is your birth year? ')
current_age = current_year - birth_year
print(f'your age is {current_age}. ')

# exercise 4 below is the examples for uses of string
name = 'santhosh kumar'
print(list(name))

# below is example for find the length in given strings
cars = 'volks wagen'
print(len(cars))

# example to get upper case in strings
cars = 'volks wagen'
print(cars.upper())

# examle to get lower case in strings
spaces = 'JUPITER'
print(spaces.lower())

# example for replace
watch = 'titan sonata'
print(watch.replace('sonata', 'police'))




