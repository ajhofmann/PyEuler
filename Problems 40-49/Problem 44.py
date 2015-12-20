## Project Euler Problem 44:
## Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference
## are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?


import time
start = time.time()

# generate a list of a lot of triangle numbers
pent_nums = {int(i*(3*i - 1)/2): i for i in range(1, 3000)}
difs = []


for i in range(1, len(pent_nums)):
    for j in range(i+1, len(pent_nums)):
            num1 = int(i*(3*i - 1)/2)
            num2 = int(j*(3*j - 1)/2)
            if num2 - num1 in pent_nums:
               if num2 + num1 in pent_nums:
                    difs.append(num2 - num1)



print(min(difs), time.time() - start)