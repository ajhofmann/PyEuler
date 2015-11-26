## Project Euler Problem 26
## Find the value of d < 1000 for which
## 1/d contains the longest recurring cycle in its decimal fraction part.

import math
# Use long division to determine when the decimal will start repeating
# only works for division by 1


def recur_len(n, remain, so_far):
    if remain == 0:
        #not a reccuring cycle
        return 0
    if remain in so_far and len(so_far) > 0:
        return len(so_far) + 1
    elif n < remain * 10:
        return recur_len(n, (10 * remain)%n, so_far + [remain])
    elif n > remain:
        return recur_len(n, 10 * remain, so_far)
    elif n < remain:
        return recur_len(n, remain%n, so_far + [remain])

greatest = (1, 1)

for i in range(1, 1000):
    cycle_len = recur_len(i, 1, [0])
    if cycle_len > greatest[1]:
        greatest = (i, cycle_len)

print(greatest)


