# A program that tells user which company registred their email address
# More popular company can/should be added
# by Aminu ahmadh
# GITHUB @AminuAhmadh



import pyinputplus as pyip

name = input("Hey, what's your name\n")
email = pyip.inputEmail(prompt=f"ok {name}, what's your email address:\n")
if email.endswith('gmail.com'):
    print(f'i see that your email address is registred with Google, {name}. that was great')
elif email.endswith('yahoo.com'):
    print(f'i see that your email address is registred wit yahoo, {name}. that was great')
else:
     print(f'i see that you have a custom email address, {name}. that was fantastic')