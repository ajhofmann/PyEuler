## Project Euler Problem 14
## What starting number under one million has the longest collatz sequence


## list of length of collatz chain for each number
## index i corresponds to chain length of number i
chain_lengths = ["undefined", 0, 1]


## finds the length of a collatz chain and adds it to the list
def collatz_chain(n):
    length = 0
    while n != 1:
        if n < len(chain_lengths):
            chain_lengths.append(length + chain_lengths[int(n)])
            return (length + chain_lengths[(int(n))])
        elif n%2 == 0:
            length += 1
            n /= 2
        else:
            length += 1
            n = n * 3 + 1
    chain_lengths.append(length)
    return length


greatest_len = 1
greatest_i = 1

for i in range(3,1000000):
    current_len = collatz_chain(i)
    if current_len > greatest_len:
        greatest_len = current_len
        greatest_i = i

print(greatest_i)