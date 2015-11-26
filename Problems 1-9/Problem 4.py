## Project Euler Problem 4
## Find the largest palindrome made from the product of two 3-digit numbers.

greatest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i*j
        if greatest < prod:
            if str(prod) == str(prod)[::-1]:
                greatest = prod
print(greatest)