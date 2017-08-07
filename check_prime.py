# -*- coding: utf-8 -*-

"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""

def convert_to_int(cmd):
    return int(cmd)

def find_factors(n):
    factors = [i for i in range(1, n + 1) if n % int(i) == 0]
    return factors

def is_prime(n):
    if len(find_factors(n)) == 1 or len(find_factors(n)) == 2:
        print('Yes! %d is prime!' % n)
        return True
    else:
        print('No! %d is not prime!' % n)
        return False

cmd = input('Enter \'exit\' or a number: ')
num = convert_to_int(cmd)
is_prime(num)
