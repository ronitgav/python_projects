"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and
printing out that many copies of the previous message. (Hint: order of
operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""

name = raw_input("Enter your name: ")
age = raw_input("Enter your age: ")
num_times = input('How many times would you like to print the subsequent message? ')
yr_born = 2017 - int(age)
turn_100 = yr_born + 100

for i in range(num_times):
    print("Hey %s, you will turn 100 in the year %s" % (name, str(turn_100)))
