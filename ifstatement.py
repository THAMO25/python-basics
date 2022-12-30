# example for if,elif,else

world = input('enter your country')
country1 = 'china'
country2 = 'india'

if (country1 == world):
    print('welcome to china')
elif (country2 == world):
    print('welcome to india')
else:
    print('cant found')

#     example for nested if

world = input('enter your country')
country1 = 'china'
country2 = 'india'

if (country1 == world):
    print('welcome to china')
    district = input('which district?:')
if (district == 'tamilnadu'):
    print("helloooo")

elif (country2 == world):
    print('welcome to india')
else:
    print('cant found')

# example of leapyear in if statement
year = int(input('enter your birth year: '))
leap_year = year % 4

if (leap_year == 0):
    print('its a leap year')
else:
    print('it is not a leap year')

# example for area of triangle
height = float(input('enter the traingle height: '))
base = float(input('enter the traingale base: '))
area_traingle = (height * base) / 2
print(f'area of triangle = {area_traingle}')

# example to find positive,negative or equal to zero
number = float(input('enter the number:'))
if (number > 0):
    print('it is a positive number')
elif (number < 0):
    print('it is a negative value')
else:
    print('it is equal to zero')

# example for finding odd or even

given_number = float(input('enter the number:'))
if given_number % 2 == 0:
    print('its a even number')
else:
    print('it is an odd number')

# example for logical operators use in if statements

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print('eligible')

    # example for logical operators use or statement

    has_high_income = False
    has_good_credit = False

    if has_high_income or has_good_credit:
        print('eligible')

# example for validating user name using if conditions
first_name = input('enter the firstname: ')
last_name = input('enter the lastname: ')

if len(first_name + last_name) > 8 and last_name.isnumeric() and first_name.isalpha():
    print('valid user')
else:
    print('not a valid user')

# examplle for eligible for vote
user_age = int(input('enter the age: '))

if (user_age >== 18):
    print('eligible for vote')
else:
    print('not eligible for vote')

# example for last digit of the number entered by user is divisible by 3 or not
num = int(input('enter the number:'))
last_digit = num % 10
if (last_digit % 3 == 0):
    print('it divisible by 3')
else:
    print('not divisible by 3')
