## Project Euler Problem 41:
## We shall say that an n-digit number is pandigital if
##  it makes use of all the digits 1 to n exactly once.
## What is the largest n-digit pandigital prime that exists?

# consider that 1 + 2 + ... + 8 + 9 = 45 and similarly up to 8 is 36
# since 36 and 45 are divisible by 3, ignore 8 or 9 digit numbers
# Also not we can ignore 2, 3, 5 and 6 digit numbers for the same reason
# Now consider any 7 digit numbers that are pandigital and check if they're prime

max = 0

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n < 9:
        return True
    if n%3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def unique_digits_no_zero(num):
    num_chars = {}
    for j in range(len(num)):
        num_chars[num[j]] = 0
        if num[j] == '0':
            return False
    if len(num_chars) == len(num):
        return True
    else: return False

for a in range(1,8):
    for b in range(1,8):
        for c in range(1,8):
            for d in range(1,8):
                for e in range(1,8):
                    for f in range(1,8):
                        for g in range(1,8):
                            num = a*(10**6) + b*(10**5) + c*(10**4) \
                                  + d*(10**3) + e*(10**2) + f*(10**1) + g
                            if num > max:
                                if unique_digits_no_zero(str(num)):
                                    if isPrime(num):
                                        max = num

print(max)

