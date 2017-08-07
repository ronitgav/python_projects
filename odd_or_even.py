"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.

2. Ask the user for two numbers: one number to check (call it num) and one
   number to divide by (check). If check divides evenly into num, tell that
   to the user. If not, print a different appropriate message.
"""

print('Choose either option 1 or option 2')
print('1: Check if odd or even')
print('2: Check if num2 divides evenly into num')

option = int(input())

if option == 1:
    num = int(input('Enter a number: '))
    if num % 2 == 0:
        if num % 4 == 0:
            print('The number is even and a multiple of 4')
        else:
            print('The number is even')
    else:
        print('The number is odd')

else:
    num = int(input('Enter a number: '))
    check = int(input('Enter a divisor: '))

    if num % check == 0:
        print('Num is divisible by check')
    else:
        print('Num is not divisible by check')
