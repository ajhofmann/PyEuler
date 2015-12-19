## Project Euler Problem 40:
## An irrational decimal fraction is created by concatenating the positive integers:

## 0.123456789101112131415161718192021...

## If dn represents the nth digit of the fractional part, find the value of the following expression.

## d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

constant = []
count = 1

while len(constant) < 1000000:
    string = str(count)
    for i in range(len(string)):
        constant.append(string[i])
    count += 1

print(int(constant[0]) * int(constant[9]) * int(constant[99])
      * int(constant[999]) * int(constant[9999])
      * int(constant[99999]) * int(constant[999999]))
