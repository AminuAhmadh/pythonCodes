# BY AMINU AHMADH
# GITHUB @AminuAhmadh

""" --- Hacker Rank Problem --- AUTHOR -- Shashank21j
An extra day is added to the calender almost every four years as February 29, 
and the day is called a leap day. It corrects the calender for the fact that our 
planet takes approximately 365.25 days to orbit the Sun. A leap year contains a leap day.

In the Gregorian Calender, three conditions are used to identify leap years:
* The year can be evenly divided by 4, is a leap year, unless:
* The year can be evenly divided by 100, it's NOT a leap year, unless:
* The year is also evenly divisible by 400. Then it is a leap year.

This means on the Gregorian Calender the years 2000 and 2400 are leap years,
while 1800, 1900, 2100, 2200, 2300 AND 2500 are not leap years.

"""

# returns True if a year is a leap year else False
def is_leaf_year(year: int):
    return (year % 4 == 0 and (year % 400 == 0 and not year % 100))