## Project Euler Problem 2:
## By considering the terms in the Fibonacci sequence whose values
## do not exceed four million, find the sum of the even-valued terms

fib_sum = 0
previous_term = 0
current_term = 1
i = 0
while i < 4000000:
    i = current_term + previous_term
    previous_term = current_term
    current_term = i
    if i%2 == 0:
        fib_sum += i

print (fib_sum)