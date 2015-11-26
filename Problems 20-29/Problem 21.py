## Project Euler Problem 21
## Evaluate the sum of all the amicable numbers under 10000.

import math

def sum_factors(n):
    factor_sum = 1
    for i in range(2, math.floor(math.sqrt(n) + 1)):
        if n%i == 0:
            factor_sum += int(n/i) + i
            if int(n/i) == i:
                factor_sum -= i
    return factor_sum

amicables = []

def amicable(n):
    factor_sum = sum_factors(n)
    if factor_sum != n and n == sum_factors(factor_sum):
        amicables.append(factor_sum)
        amicables.append(n)

for i in range(1,10000):
    if i not in amicables:
        amicable(i)

print(sum(amicables))
