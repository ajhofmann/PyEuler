## Project Euler Problem 31:
## How many different ways can £2 be made using any number of coins?
coins = [1, 2, 5, 10, 20, 50, 100, 200]

# amount of ways using a single coin
ways = 1
change_so_far = 0
import math
for cent in range(201):
    for two in range(101 - math.floor(cent/2)):
        change_so_far = cent + two*2
        for five in range(41 - math.floor((cent + two*2)/5)):
            change_so_far += five*5
            for ten in range(21 - math.floor((cent + two*2 + five*5)/10)):
                change_so_far += ten*10
                for twenty in range(11 - math.floor((cent + two*2 + five*5 + ten*10)/20)):
                    change_so_far += twenty*20
                    for fifty in range(5 - math.floor((cent + two*2 + five*5 + ten*10 + twenty*20)/50)):
                        change_so_far += fifty*50
                        for hundred in range(3 - math.floor((cent + two*2 + five*5 + ten*10 + twenty*20 + 50*fifty)/100)):
                            if (cent + two*2 + five*5 + ten*10 + twenty*20 + 50*fifty + hundred*100) == 200:
                                ways += 1



print(ways)