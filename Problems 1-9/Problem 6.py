## Project Euler Problem 6
## Find the difference between the sum of the squares of the
## first one hundred natural numbers and the square of the sum.

def sum_squares(x):
    return (x * (x + 1) * (2 * x + 1)) / 6

def square_of_sum(x):
    return ((x * (x + 1)) / 2) ** 2

print (square_of_sum(100) - sum_squares(100))