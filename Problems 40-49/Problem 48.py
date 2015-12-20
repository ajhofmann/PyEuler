## Project Euler Problem 48:
## Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
num = 0
for i in range(1, 1001):
    num += i**i

print(str(num)[len(str(num)) - 10:])