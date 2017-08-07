# -*- coding: utf-8 -*-
"""
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except with
the words in backwards order. For example, say I type the string:

  My name is Michele
  
Then I would see the string:

  Michele is name My
shown back to me.
"""

def get_rev_list(n):
    l = n.split(' ')
    l.reverse()    
    return " ".join(l)

print(get_rev_list(raw_input('Enter a list of numbers separated by spaces: ')))
