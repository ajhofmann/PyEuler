## Project Euler Problem 36:
## Find the sum of all numbers, less than one million,
## which are palindromic in base 10 and base 2

sum = 0

# converts a number into base 2
def base2_convert(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return base2_convert(n//2) + str(n%2)

# 999,999 is last palindromic number under 1 million
for i in range(1000000):
    if str(i) == str(i)[::-1]:
        base2 = base2_convert(i)
        if str(base2) == str(base2)[::-1]:
            sum += i

print(sum)