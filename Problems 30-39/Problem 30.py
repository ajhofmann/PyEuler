## Project Euler Problem 30:
## Find the sum of all the numbers that can be written as
## the sum of fifth powers of their digits.


# define powers to avoid reomputing
powers = [0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049]

# set sum = -1 to account for 1
sum = -1

# since 9^5 * 6 < 400,000 only check sixth digit below 4
for a in range(0, 4):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    for f in range(0, 10):
                        num1 = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
                        num2 = powers[a] + powers[b] + powers[c] + powers[d] + powers[e] + powers[f]
                        if num1 == num2:
                            sum += num1

print(sum)