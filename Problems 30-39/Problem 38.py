## Project Euler Problem 38
## What is the largest 1 to 9 pandigital 9-digit number that can be formed
## as the concatenated product of an integer with (1,2, ... , n) where n > 1?


# Number cannot be more than 5 digits as XXXXX*1 + XXXXX*2 = 10 numbers at least
# Also consider the number 9, giving 9, 18, 27, 36, 45 we can conclude the solution must
# start with a 9

max = 918273645

def nine_len_concat(num, n, sofar):
    if len(sofar) > 8:
        return sofar
    else:
        return nine_len_concat(num, n+1, sofar + str(num*n))

def unique_digits_no_zero(num):
    num_chars = {}
    for j in range(len(num)):
        num_chars[num[j]] = 0
        if num[j] == '0':
            return False
    if len(num_chars) == len(num):
        return True
    else: return False


for i in range(1, 10000):
    string = nine_len_concat(i, 1, '')
    if unique_digits_no_zero(string):
        if int(string) > max:
            max = int(string)

for i in range(900, 1000):
    string = nine_len_concat(i, 1, '')
    if unique_digits_no_zero(string):
        if int(string) > max:
            max = int(string)

for i in range(9000, 10000):
    string = nine_len_concat(i, 1, '')
    if unique_digits_no_zero(string):
        if int(string) > max:
            max = int(string)

print(max)
