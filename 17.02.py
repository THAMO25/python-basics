# VARIABLE-We use variable to store data temporarily in memory location.


# ex:num=10,the 10 will store in the memory and the num will be the label for the memory that we stored
# num = 10
# print(num)


# ex 1
# Name = 'john'----------string
# age = 20---------------integer
# new_patient = True-----boolean

# receiving inputs,we getting the inputs from the user by input()
# name = input('what is your name? ')
# colour = input('what is your fav colour? ')
# print(name + ' likes ' + colour)


# type converstion function it convert string which is in number format to int.if input is alphabet it throws the error
# birth_year = int(input('enter the year: '))
# age = 2022 - birth_year
# print('my age is',age)

# ex
# weight = int(input('enter the weight in pound: '))
# pound = 0.45359237 * weight
# print('kg is', weight)


# string,we use the characters inside the quotation
# name = 'i am thamo'
# print(name)
# if we want to specify the particular word in string we can use multiple quotation
# name = 'i am "thamo"'
# print(name)

# name = 'thamotharan'
#       012345678910
# print(name[1:-4])

# formated string
# f_name = 'thamo'
# l_name = 'tharan'
# print(f'{f_name} {l_name} is a coder')

# string methods
# name = 'thamotharan'
# print(len(name))

# name = 'thamoTharan'
# print(name.upper())
# print(name.lower())
# print(name.find('t'))
# print(name.replace('Tharan','tharan'))

# arithmetic operators
# +
# -
# *

# ** power
# a=3
# print(a**3)

# / divide and it gives qoutient
# a=10
# print(a/3)

# // divide and it  gives qoutient in int
# a=10
# print(a//3)

# % divides and its give remainder
# a = 1
# print(1 % 10)

# math function
# a=1.0
# print(round(a))

# list
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list, to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# tuple
# Tuple items are ordered, unchangeable, and allow duplicate values.
# method
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


# Python has two loop commands:
# while loops
# i = 1
# while i < 8:
#  print(i)
#  i =i+ 1


# ex
# secret_num = 9
# i = 0
# while i < 3:
#   num = int(input('enter the number: '))
#  if secret_num == num:
#     print('winner')
#    break
# else:
#   print('not a winner')
#  i = i + 1
