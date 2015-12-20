## Project Euler Problem 45:
## Find the next triangle number that is also pentagonal and hexagonal after 40755.

# Quadratic formula was used on the formulas for triangle and pentagonal numbers to
# determine the if a number was triangular or pentagonal backwards
import math

def tri_check(n):
    return ((1 + math.sqrt(1 + 24*n))/ 6).is_integer()

def pent_check(n):
    return ((-1 + math.sqrt(1 + 8*n))/ 2).is_integer()

tri_pent_hex_nums = []
count = 0
i = 1

while count < 3:
    num = i*(2*i -1)
    if pent_check(num) and tri_check(num):
        tri_pent_hex_nums.append(num)
        count += 1
    i += 1

print(tri_pent_hex_nums[2])