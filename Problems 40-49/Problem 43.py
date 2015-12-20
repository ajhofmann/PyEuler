## Project Euler Problem 43:
## number is 1406357289
## Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
## d2d3d4=406 is divisible by 2
## d3d4d5=063 is divisible by 3
## d4d5d6=635 is divisible by 5
## d5d6d7=357 is divisible by 7
## d6d7d8=572 is divisible by 11
## d7d8d9=728 is divisible by 13
## d8d9d10=289 is divisible by 17
## Find the sum of all 0 to 9 pandigital numbers with this property.


def unique_digits(num):
    num_chars = {}
    for j in range(len(num)):
        num_chars[num[j]] = 0
    if len(num_chars) == len(num):
        return True
    else: return False

def unique_digits_and_div_checker(num):
    num_chars = {}
    if int(num[1:4])%3 == 0 and int(num[4:7])%11 == 0 and int(num[5:8])%13 == 0:
        for j in range(len(num)):
            num_chars[num[j]] = 0
        if len(num_chars) == len(num):
            return True
    else: return False

# make lists of numbers under 999 divisble by 2, 7 and 17, then put those
# together to remove possibilites. One digit numbers have 2 zeroes

div2_temp = [i for i in range(10, 1000, 2)]
div7_temp = [i for i in range(14, 1000, 7)]
div17_temp = [i for i in range(17, 1000, 17)]
div2 = []
div7 = []
div17 = []

# filter any with 6th digit not 0 or 5 because of divide by 5 condition
# also filter any with not unique digits
for i in range(len(div7_temp)):
    string = str(div7_temp[i])
    if string[1] == '5' or string[1] == '0':
        if unique_digits(string):
            div7.append(div7_temp[i])

for i in range(len(div2_temp)):
    string = str(div2_temp[i])
    if unique_digits(string):
        div2.append(div2_temp[i])

for i in range(len(div17_temp)):
    string = str(div17_temp[i])
    if unique_digits(string):
        div17.append(div17_temp[i])

list = []

# Will produce a list of valid numbers with the first digit missing
for a in range(len(div2)):
    for b in range(len(div7)):
        for c in range(len(div17)):
            str1 = str(div2[a])
            str2 = str(div7[b])
            str3 = str(div17[c])
            if len(str1) == 2:
                str1 = '0' + str1
            if len(str2) == 2:
                str2 = '0' + str2
            if len(str3) == 2:
                str3 = '0' + str3
            if unique_digits_and_div_checker(str1+str2+str3):
                list.append(str1+str2+str3)

final_list = []

# Adds the missing digit
for i in range(len(list)):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for j in range(9):
        digits.remove(list[i][j])
    final_list.append(int(digits[0] + list[i]))

print(sum(final_list))
