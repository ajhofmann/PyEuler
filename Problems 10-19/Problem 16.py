## Project Euler Problem 16
## What is the sum of the digits of the number 2^1000?

n = str(2 ** 1000)
result = 0
for i in range(len(n)):
    result += int(n[i])

print(result)