# Tip calculator
# By Aminu Ahmadh GITHUB @AminuAhmadh


print('This is a tip calculator for a total bill')
while True:
    try:
        bill = int(input('Enter the total bil for today: ')) 
    except ValueError:
        print('Please enter correct value!')
        continue

    if bill <= 50:
        tip = 18/100 * bill
        print(f'18% tip is {round(tip)} which brings your total to {round(bill+tip)}')
        break
    elif bill >= 50 and bill <= 100:
        tip = 20/100 * bill
        print(f'20% tip is {round(tip)} which brings your total to {round(bill+tip)}')
        break
    elif bill > 100:
        tip = 25/100 * bill
        print(f'25% tip is {round(tip)} which brings your total to {round(bill+tip)}')
        break
print('thank you for the service')