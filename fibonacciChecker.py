# A program that tell you whether the number you gave it is a fibonacci number
# BY AMINU AHMADH
# GITHUB @AminuAhmadh


number = int(input('Enter a number to check if it is a Fibonacci Number: '))
n1, n2 = 0, 1
x = []
if number == 0:
    print("YES it's a Fibonacci Number")
    exit()
if number == 1:
    print("YES it's a Fibonacci Number")
    exit()

for  i in range(2, number):
    
    nth = n1 + n2
    n1 = n2
    n2 = nth
    x.append(nth)
    if sum(x[-2:]) != number:
        continue
    elif sum(x[-2:]) == number:
        print("YES it's a Fibonacci Number")
        x.append(sum(x[-2:]))
        print(x)
        break
        
# if loop finishes, then it's not a fibonacci number
if (i+1) == number and (sum(x[-2:]) != number) == True:
    print("No it's not a Fibonacci Number")
