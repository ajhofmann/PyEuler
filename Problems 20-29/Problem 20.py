## Project Euler Problem 20
## Find the sum of the digits in the number 100!

import math

n = str(math.factorial(100))

result = 0
for i in range(len(n)):
    result += int(n[i])

print(result)