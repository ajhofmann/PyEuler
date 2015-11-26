## Project Euler Problem 10
## Find the sum of all the primes below two million.

import math

def primes_under(n):
    prime_list = [2, 3]
    prime = 5
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

print(sum(primes_under(2000000)))