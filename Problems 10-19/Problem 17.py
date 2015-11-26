## Project Euler Problem 17
## If all the numbers from 1 to 1000 (one thousand) inclusive were
## written out in words, how many letters would be used?

import math

# defines letters for 0 <= n <= 9
singles = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]

# defines letters for 10 <= n <= 19
tens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

# defines letters in tens place of 20 <= n <= 90
tens_place = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

# finds letters in a number under 100
def letters_under_100(n):
    if n < 10:
        return singles[n]
    elif n < 20:
        return tens[n-10]
    else:
        return tens_place[math.floor(n/10)] + singles[n%10]


# finds letters in a number under 1000 inclusive
# 7 is letters in the word "hundred" and 10 in "hundred and"
def letters_under_1000(n):
    if n == 1000:
        return 11
    if n%100 == 0:
        return 7 + singles[(int(n/100))]
    if n < 100:
        return letters_under_100(n)
    else:
        return 10 + singles[int(n/100)] + letters_under_100(n%100)

print(sum(letters_under_1000(i) for i in range(1, 1001)))