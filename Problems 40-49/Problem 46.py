## Project Euler Problem 46:
## What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n < 9:
        return True
    if n%3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def satisfies(n):
    for i in range(len(odd_primes)):
        if (math.sqrt((n - odd_primes[i])/2)).is_integer():
            return True
    return False


odd_primes = [3]
i = 3

while True:
    if isPrime(i):
        odd_primes.append(i)
        i += 2
    elif satisfies(i):
        i += 2
    else:
        print(i)
        break