## Project Euler Problem 58:

## Starting with 1 and spiralling anticlockwise in the following way,
##  a square spiral with side length 7 is formed.

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

## It is interesting to note that the odd squares lie along the bottom right diagonal,
## but what is more interesting is that 8 out of the 13 numbers lying along both
## diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

## If one complete new layer is wrapped around the spiral above,
## a square spiral with side length 9 will be formed. If this process is continued,
## what is the side length of the square spiral for which the ratio of primes along both
## diagonals first falls below 10%?


# the formula for the line up left is odd square numbers (9, 25, 49 ... n^2)
# the formula for the line up right is (odd square numbers - (n-1)) (7, 21, 43 ... n^2 - (n-1))
# the formula for the line down left is (odd square number - 2(n-1)) (5, 17, 37 ... n^2 - 2(n-1))
# the formula for the line down left is (odd square number - 3(n-1)) (3, 13, 31 ... n^2 - 3(n-1))



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

# for initial 7 length square
total = 13
primes = 8

# Don't test n^2, cant be prime
while primes / total > .1:
    total += 4
    n = (total + 1) /2
    primes += isPrime(n**2 - (n-1)) + isPrime(n**2 - 2*(n-1)) + isPrime(n**2 - 3*(n-1))

print((total+1) / 2)