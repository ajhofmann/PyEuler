## Project Euler Problem 37:
## The number 3797 has an interesting property. Being prime itself, it is possible
## to continuously remove digits from left to right, and remain prime at each stage:
## 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

## Find the sum of the only eleven primes that are both truncatable
## from left to right and right to left.

import math
import time
start = time.time()

trunc_primes = []

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

# if the prime starts with 4, 6, 8, 0 then non of them are prime
# if it doesnt start with those digits and has them then it will eventually
# truncate to an even number

for i in range(len(old_primes)):
    string = str(old_primes[i])
    if not ('4' in string or '6' in string or '8' in string or '0' in string):
        primes.append(old_primes[i])

def truncable(left, right):
    if len(left) == 1:
        return True
    new_left = left[:len(left) - 1]
    new_right = right[1:]
    if int(new_left) in primes and int(new_right) in primes:
        return truncable(new_left, new_right)
    else:
        return False

# don't check 2, 3, 5, 7
for i in range(4, len(primes)):
    if truncable(str(primes[i]), str(primes[i])):
        trunc_primes.append(primes[i])

print(sum(trunc_primes), time.time() - start)
