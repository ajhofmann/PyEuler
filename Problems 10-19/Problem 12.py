## Project Euler Problem 12
## What is the value of the first triangle number to have over five hundred divisors?
import math

# determines factors of n
def factors(n):
    factors = 0
    for i in range(1, math.floor(math.sqrt(n))):
        if n%i == 0:
            factors += 2
    return factors

# determines the nth triangle number
def triangle_num(n):
    return (n * (n+1)) / 2

i = 1
while factors(triangle_num(i)) < 500:
    i += 1

print(triangle_num(i))