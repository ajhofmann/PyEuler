## Project Euler Problem 25
## What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math

previous_term = 1
current_term = 1
i = 0
index = 2
while math.log(current_term, 10 ** 999) <= 1:
    i = current_term + previous_term
    previous_term = current_term
    current_term = i
    index += 1

print(index)