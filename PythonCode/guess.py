# This is a guess the number game.
# by aminu ahmadh
# GITHUB @AminuAhmadh



import random


secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


# another one with infinite guesses till user gets it right
number = random.randint(1, 50)
print('i am thinking of a number between 1 and 50')
while True:
    guess = int(input('take a guess '))
    if guess > number:
        print('it is lower than that')
    elif guess < number:
        print('it is higher than that')
    elif guess == number:
        print('You guessed it right')
        break
