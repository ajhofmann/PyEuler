## Project Euler Problem 33:
## The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting
## to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
## is obtained by cancelling the 9s.

## We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

## There are exactly four non-trivial examples of this type of fraction, less
## than one in value, and containing two digits in the numerator and denominator.

## If the product of these four fractions is given in its lowest common terms,
## find the value of the denominator.

fractions = []
numerator = 10
denominator = 11
for i in range(10, 100):
    for j in range(i + 1, 100):
        if not int(str(j)[1]) == 0:
            if i/j == int(str(i)[0])/int(str(j)[1]) and str(i)[1] == str(j)[0]:
                fractions.append(i)
                fractions.append(j)

print(fractions[0] * fractions[2] * fractions[4] * fractions[6])
print(" over ")
print(fractions[1] * fractions[3] * fractions[5] * fractions[7])