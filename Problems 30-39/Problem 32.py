## Project Euler Problem 32:
## Find the sum of all products whose multiplicand/multiplier/product
## identity can be written as a 1 through 9 pandigital

# Only need to test 2 digits * 3 digits and 1 digit * 4 digits, no others will have 9 digits

numbers = []
four_dig_ind = 0
three_dig_ind = 0
two_dig_ind = 9
one_dig_ind = 0
products = []

import functools

def unique_digits_no_zero(n):
    num = str(n)
    num_chars = {}
    for j in range(len(num)):
        num_chars[num[j]] = 0
        if num[j] == '0':
            return False
    if len(num_chars) == len(num):
        return True
    else: return False

for i in range(1, 9876):
    if unique_digits_no_zero(i):
        if i == 1234:
            four_dig_ind = len(numbers)
        if i == 123:
            three_dig_ind = len(numbers)
        numbers.append(i)

for i in range(one_dig_ind, two_dig_ind):
    for j in range(four_dig_ind, len(numbers)):
        string = str(numbers[i]) + str(numbers[j]) + str(numbers[i] * numbers[j])
        number = int(string)
        if len(string) == 9 and unique_digits_no_zero(number):
             if numbers[i] * numbers[j] not in products:
                products.append(numbers[i] * numbers[j])

for i in range(two_dig_ind, three_dig_ind):
    for j in range(three_dig_ind, four_dig_ind):
        string = str(numbers[i]) + str(numbers[j]) + str(numbers[i] * numbers[j])
        number = int(string)
        if len(string) == 9 and unique_digits_no_zero(number):
            if numbers[i] * numbers[j] not in products:
                products.append(numbers[i] * numbers[j])


print(sum(products))
