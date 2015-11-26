## Project Euler Problem 7
## What is the 10001st prime number?

import math

def nth_prime(n):
    prime_list = [2, 3]
    prime = 5
    i = 2
    while i < n:
        for j in range(0, i):
            if prime%prime_list[j] == 0:
                prime += 2
                break
            if prime_list[j] >= (math.floor (math.sqrt(prime)) + 1):
                prime_list.append(prime)
                i += 1
                prime+= 2
                break
    return prime_list[i-1]


print(nth_prime(10001))