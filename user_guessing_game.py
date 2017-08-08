# -*- coding: utf-8 -*-

"""
In a previous exercise, we’ve written a program that “knows” a number and asks
a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in
your head a number between 0 and 100. The program will guess a number, and you,
the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it
took to get your number.

As the writer of this program, you will have to choose how your program will
strategically guess. A naive strategy can be to simply start the guessing at 1,
and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an
optimal guessing strategy. An alternate strategy might be to guess 50 (right
in the middle of the range), and then increase / decrease by 1 as needed.
After you’ve written the program, try to find the optimal strategy! (We’ll
talk about what is the optimal one next week with the solution.)
"""
import random

number_to_guess = int(raw_input('Enter a number between 0 and 100: '))

maximum = 100
minimum = 0
comp_guess = random.randint(0, 100)

while True:
    response = raw_input('%d : Low, High or Correct ? ' % comp_guess)
    if response == 'Too low' or response == 'Low':
        minimum = comp_guess
        comp_guess = random.randint(minimum, maximum)
    elif response == 'Too high' or response == 'High':
        maximum = comp_guess
        comp_guess = random.randint(minimum, maximum)
    else:
        print('GOOD JOB! YOU GOT THE NUMBER RIGHT!')
        break

    

    
