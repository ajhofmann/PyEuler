## Project Euler Problem 39:
## If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
## For which value of p ≤ 1000, is the number of solutions maximised?

# First generate all unique right triangles using Euclids formula
# with condition m and n are coprime, m > n and m - n is odd

import math
import time
start = time.time()

perimeters = []
max_solutions = 0
max_p = 0

def valid_perimeter(m, n):
    if math.gcd(m, n) == 1 and (m-n)%2 == 1:
        # a+b+c from euclids formula
        perimeters.append(2 * (m**2) + 2 * m * n)

# if m = 24 and n = 1 then 2m^2 + 2mn > 1000 so stop considering m > 24

for m in range(1, 24):
    for n in range(1, m-1):
        valid_perimeter(m, n)

# now with the list of perimeters go from numbers 1 -> 1000 and see which is most
# divisible. If a perimeter divides a number n 3 times, then there is 3 different
# triangles that can go into it, ie 70/210 has [70, 140, 210]

for i in range(1, 1000):
    solutions = 0
    for j in range(len(perimeters)):
        if i%perimeters[j] == 0:
            solutions += i/perimeters[j]
    if solutions > max_solutions:
        max_solutions = solutions
        max_p = i

print(max_p, time.time() - start)

