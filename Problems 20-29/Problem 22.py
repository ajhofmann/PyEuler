## Project Euler Problem 22
## sort p022_names.txt into alphabetical order.
## Work out the alphabetical value for each name
## ex: COLIN = 3 + 15 + 12 + 9 + 14 = 53
## multiply this number by the position in the list
## return the sum of all of the scores of all nmaes

file = open("p022_names.txt", "r")
names = file.read().split(',')
names.sort()

total_score = 0
for i in range(len(names)):
    name = list(names[i])
    sum_letters = 0
    # don't count 1st and last letters as they are ""
    for j in range(1, len(name) - 1):
        sum_letters += ord(name[j]) - 64
    total_score += sum_letters * (i + 1)

print(total_score)