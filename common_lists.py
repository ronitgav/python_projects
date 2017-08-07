# -*- coding: utf-8 -*-
"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1) Randomly generate two lists to test this
2) Write this in one line of Python (don’t worry if you
  can’t figure this out at this point - we’ll get to it soon)
"""
from random import randint
list_comm = []
[list_comm.append(i) for i in set(randint(0, 100) for p in range(0, randint(0, 100))).intersection(set(randint(0, 100) for p in range(0, randint(0, 100))))]
print(list_comm)
