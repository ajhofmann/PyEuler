## Project Euler Problem 15
## How many routes are there from the top left corner moving only
## right and down through a 20×20 grid?


grid = [[1 for i in range(21)] for i in range(21)]

## uses the fact that the first row will be always br 1 as there is only one way to move
## right through it. Also the ways to get to an intersection are the ways to get to the
## left of it plus the ways to get to the top of it. Top row and first column will always
## be one so use this fact to move down creating rows
for i in range(1, 21):
    for j in range(1, 21):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid[20][20])