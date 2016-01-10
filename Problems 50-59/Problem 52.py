## Project Euler Problem 52:
## It can be seen that the number, 125874, and its double, 251748, contain exactly the
##  same digits, but in a different order.

##Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
## contain the same digits.

def isPermute(a, b):
        return sorted(a) == sorted(b)

i = 1
while True:
    x = str(i)
    if isPermute(x, str(2*i)) and isPermute(x, str(3*i)) and isPermute(x, str(4*i))\
            and isPermute(x, str(5*i)) and isPermute(x, str(6*i)):
        print(i)
        break
    i += 1