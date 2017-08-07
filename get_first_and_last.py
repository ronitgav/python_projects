"""
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
first and last elements of the given list. For practice, write this code
inside a function.
"""

def get_first_and_last(n):
    list1 = [int(i) for i in n.split(' ')]
    fin_list = [list1[0], list1[len(list1)-1]]
    return fin_list

print(get_first_and_last(raw_input('Enter a list of numbers separated by a space: ')))
