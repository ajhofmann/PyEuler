## Project Euler Problem 34:
## Find the sum of all numbers which are equal to the sum of the factorial of their digits.
## 2 and 1 are not sums and thus not included

## 9! * 7 < 9,999,999 so use this as an upper bound since factorials will no
## longer go high enough
factorials_under_10 = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

total = 0

for i in range(10, 2540160):
    sum = 0
    word = str(i)
    for j in range(len(word)):
        sum += factorials_under_10[int(word[j])]
    if sum == i:
        total += i

print(total)