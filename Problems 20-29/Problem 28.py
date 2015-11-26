## Project Euler Problem 28:
## Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001
# spiral formed in the same way?

## in a 1001*1001 spiral, it extends 500 up-right, up-left, down-right, down-left
# the formula for the line up left is odd square numbers (9, 25, 49 ... n^2)
# the formula for the line up right is (odd square numbers - (n-1)) (7, 21, 43 ... n^2 - (n-1))
# the formula for the line down left is (odd square number - 2(n-1)) (5, 17, 37 ... n^2 - 2(n-1))
# the formula for the line down left is (odd square number - 3(n-1)) (3, 13, 31 ... n^2 - 3(n-1))
# adding all the numbers in a layer gives 4n^2 - 6(n-1)

sum = 1

for i in range(3, 1003, 2):
    sum += 4* i ** 2 - 6*(i-1)

print(sum)