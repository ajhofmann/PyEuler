## Project Euler Problem 50:
## The longest sum of consecutive primes below one-thousand that adds to
## a prime, contains 21 terms, and is equal to 953.
## Which prime, below one-million, can be written as the sum of the most consecutive primes?

max = 21
num = 953

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

# Since we know the prime must be under 1,000,000 and they must be consecutive
# only consider primes under 1,000,000/20
primes = primes_under(50000)
leng = len(primes)
broke = True

for i in range(leng):
    sumsofar = primes[i]
    count = 1
    temp_max = 0
    while sumsofar < 1000000 and count+i < leng:
        if isPrime(sumsofar):
            temp_max = count
        sumsofar += primes[count + i]
        count += 1
    if temp_max > max:
        max = temp_max
        num = sumsofar - primes[count+i-1]

print(max, num)