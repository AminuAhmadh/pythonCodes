# A very fun and entertaining dice rolling game
# By Aminu Ahmadh
# GITHUB @AminuAhmadh

# lmport some libraries
import random, time, pyinputplus
import seaborn as se


print('YOU ARE PLAYING WITH A COMPUTER')
print("THE FIRST TO REACH '50' WINS")
print()

# dict to store progress
scores = dict({'Your Wins': 0, 'Computer Wins': 0})

# call to roll
def roll():
    rolled = random.randint(1,6)
    return rolled

while True:
    question = pyinputplus.inputYesNo('Are You Ready? \n')
    if question.lower() == 'no':
        break
    else:
        while True:
            print("Press Any Key to Roll")
            prompt = pyinputplus.inputStr()
            if prompt:
                my_roll = roll()
                scores['Your Wins'] += my_roll
                print("YOU ROLLED:", my_roll)
                time.sleep(1)
                print(scores)
                time.sleep(1)
                print()
                if scores['Your Wins'] >= 50:
                    print("Yay! You Won.")
                    break
                comp_roll = roll()
                scores['Computer Wins'] += comp_roll
                print("COMPUTER ROLLED:", comp_roll)
                time.sleep(1)
                print(scores)
                time.sleep(1)
                print()
                if scores['Computer Wins'] >= 50:
                    print("Nay! You Lost.")
                    break
                continue
    play_again = pyinputplus.inputYesNo('Play Again? \n')
    if play_again.lower() == 'yes':
        scores = dict({'Your Wins': 0, 'Computer Wins': 0})
        continue
    else:
        break