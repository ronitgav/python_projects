# -*- coding: utf-8 -*-
"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right. (Hint: remember to use the user input lessons from
                             the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends,
print this out.
"""

import random

print('This is a guessing game or \'exit\' when you want to quit')
cmd = True
count = 0

number = random.randint(1, 9)

while cmd == True:
    guess = raw_input("Guess a number: ")
    if str(guess) == "exit":
        cmd = False
        break

    guess = int(guess)
    if guess < number:
        print('Too low! Try again')
        count += 1
    elif guess > number:
        print('Too high! Try again')
        count += 1
    else:
        count += 1
        print('Exactly right! You took %d guesses' % count)
        cmd = False
