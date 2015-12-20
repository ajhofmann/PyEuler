## Project Euler Problem 49:
## The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by
## 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each
##  of the 4-digit numbers are permutations of one another.

## There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting
## this property, but there is one other 4-digit increasing sequence.

## What 12-digit number do you form by concatenating the three terms in this sequence?

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n < 9:
        return True
    if n%3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def isPermute(a, b):
        return sorted(a) == sorted(b)

def isSequence(list):
    difs = {}
    for j in range(1, len(list)):
        if (list[j] - list[0])/2 in difs:
            print(list[0], difs[(list[j] - list[0])/2], list[j])
        difs[list[j] - list[0]] = list[j]

primes = [i for i in range(1000, 10000) if isPrime(i)]

for i in range(len(primes)):
    sequence = [primes[i]]
    for j in range(i + 1, len(primes)):
        if isPermute(str(primes[i]), str(primes[j])):
            sequence.append(primes[j])
    isSequence(sequence)




