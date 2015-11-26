## Project Euler Problem 23
## Find the sum of all the positive integers which
## cannot be written as the sum of two abundant numbers.

import math
import time

start = time.time()

abundants = {}
total_sum = 0

def sum_factors(n):
    factor_sum = 1
    for i in range(2, math.floor(math.sqrt(n) + 1)):
        if n%i == 0:
            factor_sum += int(n/i) + i
            if int(n/i) == i:
                factor_sum -= i
    return factor_sum

def abundants_under(n):
    for i in range(1, n):
        if i < sum_factors(i):
            abundants[i] = i

abundants_under(28123)

for i in range(1, 28124):
    found = False
    for j in range(i):
        if j in abundants and (i - j) in abundants:
            found = True
            break
    if not found:
        total_sum += i

print(total_sum, time.time() - start)
