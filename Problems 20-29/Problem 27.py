## Project Euler Problem 27:
##Considering quadratics of the form:
# n² + an + b, where |a| < 1000 and |b| < 1000
## where |n| is the modulus/absolute value of n
## e.g. |11| = 11 and |−4| = 4
## Find the product of the coefficients, a and b, for the quadratic expression
## that produces the maximum number of primes for consecutive values
## of n, starting with n = 0.

import math



def is_prime(n):
    if n < 2:
        return False
    for i in range(math.floor(math.sqrt(n)), 1, -1):
        if n%i == 0:
            return False
    return True

# determines if all of n, from n to 0 are prime for a and b
def more_prime(a, b, n):
    for i in range(n, -1, -1):
        if not is_prime(i ** 2 + a*i + b):
            return False
    return True

def max_prime(a, b, n):
    while True:
        if is_prime(n ** 2 + a*n + b):
            n += 1
        else:
            break
    return n - 1

max_primes = 0
max_a = 0
max_b = 0

for a in range(-999, 1000, 2):
    for b in range(-999, 1000, 2):
        if more_prime(a, b, max_primes):
            max_primes = max_prime(a, b, max_primes)
            max_a = a
            max_b = b
            print(a, b, max_primes)


print(max_a, max_b, max_primes)
print(max_a * max_b)




