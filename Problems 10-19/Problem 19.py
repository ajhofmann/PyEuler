## Project Euler Problem 19
## How many Sundays fell on the first of the month during
##  the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# cumulative days in a year i.e the day that is the start of each month
normal_year = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
leap_year = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]

# 1901 started on a tuesday so in year 1 (day mod 7) = 6 is a sunday
first_sunday = 6
# on a normal year, sunday moves forward 1 day (requires (day mod 7) = start_day - 1
# on a leap year, sunday moves forward 2 days (requires (day mod 7) = start_day - 2

year = 1901
day_of_year = 1
first_sundays = 0

while year < 2001:
    if day_of_year > 366:
        day_of_year = 1
        if year%4 == 0:
            first_sunday -= 2
        else:
            first_sunday -= 1
        year += 1
    if first_sunday < 0:
        first_sunday += 7
    if year%4 == 0:
        if day_of_year in leap_year and day_of_year%7 == first_sunday:
            first_sundays += 1
    elif day_of_year in normal_year and day_of_year%7 == first_sunday:
        first_sundays += 1
    day_of_year += 1


print(first_sundays)