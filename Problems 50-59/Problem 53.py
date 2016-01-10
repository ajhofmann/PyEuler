## Project Euler Problem 53:
## How many, not necessarily distinct, values of  nCr, for
## 1 ≤ n ≤ 100, are greater than one-million?

import math

factorials = [math.factorial(x) for x in range(101)]
count = 0

def nCr(n, r):
    return factorials[n] / (factorials[r] * factorials[n-r])

# Given in question that n >= 23

for i in range(23, 101):
    for j in range(i):
        if nCr(i, j) > 1000000:
            count += 1

print(count)