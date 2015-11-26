## Project Euler Problem 3
## What is the largest prime factor of the number 600851475143?

num = 600851475143
factor = 2

while num != factor:
    if num%factor == 0:
        num = num/factor
        factor = 2
    else:
        factor += 1

print (num)