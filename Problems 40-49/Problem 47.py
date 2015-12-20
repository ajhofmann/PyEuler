## Project Euler Problem 47:
## Find the first four consecutive integers
## to have four distinct prime factors. What is the first of these numbers?

import math
import time

start = time.time()

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

# minimum amount of divisors is 2*3*5*prime so only generate primes
# that are max/30

max = 10000
primes = primes_under(max)

counter = 0


for i in range(1, max*30):
    divisors = 0
    num = i
    for j in range(len(primes)):
        if num%primes[j] == 0:
            num /= primes[j]
            divisors += 1
        if primes[j] > num:
            break
    if divisors == 4:
        counter += 1
    else:
        counter = 0
    if counter == 4:
        print(i-3)
        break

print(time.time() - start)