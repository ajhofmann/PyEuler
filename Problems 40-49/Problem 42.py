## Project Euler Problem 42:

## By converting each letter in a word to a number corresponding to its alphabetical position and
## adding these values we form a word value.

## If the word value is a triangle number then we shall call the word a triangle word.

## Using words.txt, a 16K text file
## containing nearly two-thousand common English words, how many are triangle words?

# Assuming the max word is 20 letters, and average word value is 13 we don't need
# triangle numbers higher than 260. t23 = 276 so use this as a stopping point

tri_nums = [int(i*(i+1)/2) for i in range(1, 24)]

# dictionary of letter to char
alphabet = {chr(i+64): i for i in range(1, 27)}

file = open("words.txt", "r")
words = file.read().split(',')

count = 0

# since the text file has quotes around words, ignore first and last chars
for i in range(len(words)):
    word_val = 0
    for j in range(1, len(words[i]) - 1):
        word_val += alphabet[words[i][j]]
    if word_val in tri_nums:
        count += 1

print(count)