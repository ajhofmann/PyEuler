## Project Euler Problem 5
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

smallest = 1
j = 1

for i in range (2,20):
    if smallest%i != 0:
        while i ** j < 20:
            j += 1
        smallest = smallest * (i ** (j-1))
        j = 1

print(smallest)