## Project Euler Problem 35:
## The number, 197, is called a circular prime because all rotations
## of the digits: 197, 971, and 719, are themselves prime.

## How many circular primes are there below one million?

import math

## start list at 2 as primes 2 and 5 will be filtered
count = 2

# primes under calculator with modification to filter any numbers
# with 2, 4, 5, 6, 8, 0 as they wont be cyclic


def primes_under(n):
    prime_list = [2, 3, 5]
    prime = 7
    while prime < n:
        for j in range(0, (len(prime_list))):
            if prime%prime_list[j] == 0:
                prime += 2
                break
            if prime_list[j] >= (math.floor (math.sqrt(prime)) + 1):
                prime_list.append(prime)
                prime+= 2
                break
    return prime_list


old_primes = (primes_under(1000000))
primes = []

for i in range(len(old_primes)):
    string = str(old_primes[i])
    if not ('2' in string or '4' in string or '5' in string or '6' in string or '8' in string or '0' in string):
        primes.append(old_primes[i])

for i in range(len(primes)):
    num = str(primes[i])
    counter = 0
    for j in range(len(num)):
        num = num[len(num)-1] + num[:len(num)-1]
        if int(num) in primes:
            counter += 1
    if counter == len(num):
        count += 1

print(count)