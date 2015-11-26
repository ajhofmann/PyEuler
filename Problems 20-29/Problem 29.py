## Project Euler Problem 29:
## How many distinct terms are in the sequence generated
## by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

terms = {}

for a in range(2, 101):
    for b in range(2, 101):
        terms[a**b] = a ** b

print(len(terms))