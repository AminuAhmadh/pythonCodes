# A program that summarizes Your Biography Information you gave it
# By Aminu Ahmadh
# GITHUB @AminuAhmadh


from datetime import date
import pyinputplus
import pandas as pd 


full_name = pyinputplus.inputStr(prompt='what is your Full Name: ', blockRegexes=[r'[0123456789]$', 'Please enter a valid response'] )
address = pyinputplus.inputStr(prompt='Your address: ')
month = pyinputplus.inputStr(prompt='which month were you born: ',  blockRegexes=[r'[0123456789]$', 'Please enter a Name not Number'] )
m = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12], index=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
year = pyinputplus.inputNum(prompt='which year were you born: ')
day = pyinputplus.inputNum(prompt='which day of the month were you born: ')
nationality = pyinputplus.inputStr(prompt='which country are you from: ', blockRegexes=[r'[0123456789]$', 'Please enter a valid response'])
state = pyinputplus.inputStr(prompt='Enter your state: ', blockRegexes=[r'[0123456789]$', 'Please enter a valid response'])
employment_status = pyinputplus.inputYesNo(prompt='Are you employed? ')
if employment_status == 'yes':
    job = pyinputplus.inputStr(prompt='Enter your job: ', blockRegexes=[r'[0123456789]$', 'Please enter a valid response'])
else:
    pass
hobby = pyinputplus.inputStr(prompt="what is your hobby? ", blockRegexes=[r'[0123456789]$', 'Please enter a valid response'])
vision = pyinputplus.inputStr(prompt='where do you want to see yourself in the future (GOAL)? ', blockRegexes=[r'[0123456789]$', 'Please enter a valid response'])
print()

t1 = date(year,  m[month[:3]], day )
t2 = date.today()
age = t2 - t1
final_age = age//365
fa = str(final_age)

print('Your Biography Summary...')
print()
print(f'FULL NAME:- {full_name}')
print(f'Address:- {address} ')
print(f'DOB:- {month} {str(day)}, {year} ')
print('AGE:- ',fa[:3],'years old')
print(f'From:- {state}, {nationality} ')
if employment_status == 'yes':
    print(f'Employment:- {job} ')
else:
    pass
print(f'Hobby:- {hobby} ')
print(f'Vision:- {vision} ')
print('Copyright', end=" ")
print(t2)