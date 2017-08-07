# -*- coding: utf-8 -*-

"""
Write a program (function!) that takes a list and returns a new
list that contains all the elements of the first list minus all the
duplicates.

Extras:

1) Write two different functions to do this - one using a loop and
   constructing a list, and another using sets.
2) Go back and do Exercise 5 using sets, and write the solution for that in
    a different function.
    """

def first_function(n):
    nums = list(set([int(i) for i in n.split(' ')]))
    return nums

print(first_function(raw_input('Enter a sequence of numbers separated by a space: ')))
