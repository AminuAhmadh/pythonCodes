# A random password generator by Aminu Ahmadh
# github @AminuAhmadh


import random

number = [x for x in range(10)]
lowerAlpha = 'abcdefghijklmnopqrstuvwxyz'
upperAlpha = lowerAlpha.upper()
special_character = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '?,', '<>']
password = []
for i in range(3):
    password.append(random.choice(str(number)))
    password.append(random.choice(lowerAlpha))
    password.append(random.choice(upperAlpha))
    password.append(random.choice(special_character))

random.shuffle(password)
generatedPassword =  ''.join(password)
print(generatedPassword)
