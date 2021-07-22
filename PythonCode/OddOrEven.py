name = input("hello, good day stranger. You haven't tell me your name. What is your name? ") # Welcomes User
print('OK,', name)
while True:
    try:
        number = int(input('what number are you thinking: '))
    except:
        print("Please tell me the number you are thinking not text or float") # incase User type in string or float
        continue
    if number % 2 == 0:
        print('That is an Even Number')
        prompt = input('Play Again?  ("YES/NO")  ').lower() # Ask user if she will like to play again.
        if prompt == "yes":
            pass
        else:
            break
    else:
        print('That is an Odd Number')
        prompt = input('Play Again?  ("YES/NO")  ').lower()
        if prompt == "yes":
            pass
        else:
            break

''' Another way to do it using a module called pyinputplus'''

import pyinputplus as pyip

Name = pyip.inputStr(prompt="hello, good day stranger. You haven't tell me your name. What is your name? ")
print('OK', Name)
while True:
    num = pyip.inputInt(prompt='what number are you thinking: ')
    if num % 2 == 0:
        print('That is an Even Number')
        Playagain = pyip.inputYesNo(prompt='Play again? ')
        if Playagain == 'yes':
            pass
        else:
            break
    else:
        print('That is an Odd Number')
        Playagain = pyip.inputYesNo(prompt='Play again? ')
        if Playagain == 'yes':
            pass
        else:
            break
