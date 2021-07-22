# A very fun and entertaining dice rolling game
# By Aminu Ahmadh
# GITHUB @AminuAhmadh


import random, time, pyinputplus
import pandas

print('YOU ARE PLAYING WITH A COMPUTER')
print("THE FIRST TO REACH '50' WINS")
print()

win = pandas.Series ({'MY WINS': 0, 'COMPUTER WINS': 0 })
while True:
    myWin = 0
    computerWin = 0

    question = pyinputplus.inputYesNo('wanna roll a dice? \n')
    if question == 'yes':
        for i in range(50):
            print()
            roll = pyinputplus.inputChoice(['roll', 'r'], prompt='Enter "ROLL" or "R" to roll: ').lower()
            print()
            if roll == 'roll' or 'r':
                dice_roll = random.randint(1,6)
                print(f'you rolled: {dice_roll} ')
                myWin += dice_roll
                print('my progress:',myWin)
                print()
                time.sleep(0.5)
                comp_dice = random.randint(1,6)
                print(f'Computer rolled: {comp_dice} ')
                computerWin += comp_dice
                print(f'computer progress:',computerWin)
                if myWin >= 50:
                    print()
                    print('You Won! Congratulations.')
                    win['MY WINS'] += 1
                    break
                elif computerWin >= 50:
                    print()
                    print('Computer Won!')
                    win['COMPUTER WINS'] += 1
                    break
                continue

    elif question == 'no':
        exit
    print()
    print('My total wins:', str(win['MY WINS']))
    print('Computer total wins:', str(win['COMPUTER WINS']))
    roll_again = pyinputplus.inputYesNo(prompt='wanna roll again? ')
    if roll_again =='y':
        continue
    else:
        break
