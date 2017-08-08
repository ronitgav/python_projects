# -*- coding: utf-8 -*-

"""
Given two .txt files that have lists of numbers in them, find the numbers that
are overlapping. One .txt file has a list of all prime numbers under 1000, and
the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other
 number. And yes, happy numbers are a real thing in mathematics - you can look
 it up on Wikipedia. The explanation is easier with an example, which I will
 describe below.)
 """

with open('primenums.txt', "r") as infile:
    set_of_prime_nums = set([int(i) for i in infile.read().splitlines()])

with open('happynums.txt', 'r') as file2:
    set_of_happy_nums = set([int(i) for i in file2.read().splitlines()])

print(sorted(list(set_of_prime_nums.intersection(set_of_happy_nums))))

