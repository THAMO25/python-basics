# example for for loop

for number in range(10, 20, 2):
    print(f'even number: {number}')

# finding square root
#  ** exponent operator

number = [1, 2, 3, 4, 5]
for sr in number:
    i = sr ** 3
    print(f'square root sr is: {i}')

# ecample
prices = [10, 20, 30]
number_of_products = [1, 2, 3]
total = 0
total_product = 0
totals = 0
for p in prices:
    total = total + p
print(f'total is: {total}')
for q in number_of_products:
    total_product = total_product + q
print(f'total product: {total_product}')
totals = total + total_product
print(f'total is: {totals}')