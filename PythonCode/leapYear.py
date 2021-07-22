# A PROGRAM THAT TELLS IF YEAR IS A LEAP YEAR OR NOT.
# BY AMINU AHMADH
# GITHUB @AminuAhmadh

leapyear = [x for  x in range(0, 100000) if x % 4 == 0] # pattern to recognize Leap year
while True:
    try:
        year = int(input('Enter a year to CHECK if it is a Leap Year or not: \n')) 
    except:
        print('Year Must be a number/valid number') # incase user entered str or invalid input
        continue
    if year in leapyear: 
        print('YES!', year, 'is a leap Year.')
        break
    else:
        print(year, 'is not a leap year, SORRY.')
        break