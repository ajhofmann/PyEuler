## Project Euler Problem 9
## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.

import math

for a in range(500, 1, -1):
    for b in range(a, 1, -1):
        if (a + b + math.sqrt(a**2 + b**2)) == 1000:
            print(a*b*(math.sqrt(a**2 + b**2)))
            break