## Project Euler Problem 24
## What is the millionth lexicographic permutation of the
## digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math
import time

start = time.time()

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_number = []

# the number of permutations for the nth digit is equal to n!, assuming
# the previous digits are fixed. Since it is sorted numerically, consider
# the max number in the digit without exceeding the 1,000,000 permutation

permutation = 0

for i in range(9, -1, -1):
    j = 0
    while (j + 1) * math.factorial(i) + permutation < 1000000:
        j += 1
    permutation += math.factorial(i) * j
    new_number.append(nums[j])
    del nums[j]

print(new_number, time.time() - start)