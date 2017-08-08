# -*- coding: utf-8 -*-

"""
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase letters,
numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a
main method.

Extra:

=> Ask the user how strong they want their password to be. For weak passwords,
    pick a word or two from a list.

"""
import string
import random

def determine_password_strength(sent):
    return sent

def chooseFromWeak():
    list_of_weak_words = ['cat123', 'dog3456', 'apple132453', 'love9796']
    return list_of_weak_words[random.randint(0, len(list_of_weak_words))]

def chooseFromMed():
    pwd = ''.join([list(string.letters)[random.randint(0, len(string.letters)-1)] for i in range(0, 3)])
    nums = ''.join([str(random.randint(0, 9)) for i in range(0,3)])
    pwd += nums
    return pwd

def chooseFromStrong():
    pwd = ''.join([list(string.letters)[random.randint(0, len(string.letters)-1)] for i in range(0, random.randint(0,9))])
    nums = ''.join([str(random.randint(0, 9)) for i in range(0,random.randint(0,9))])
    syms = ['!', '@', '.', '#', '%', '^', '&', '*', '(', ')']
    symbols = ''.join([syms[i] for i in range(0, random.randint(0,len(syms)-1))])
    pwd += nums
    pwd += symbols
    return pwd

if __name__ == '__main__':
    #start main method
    print('Enter strength of desired password or type \'exit\'')

    while True:
        strength = str(determine_password_strength(raw_input('How strong would you like your password: ')))

        #if weak, choose from weak words
        if strength == 'weak':
            print(chooseFromWeak())
        elif strength == 'medium':
            print(chooseFromMed())
        elif strength == 'strong':
            print(chooseFromStrong())
        elif strength == 'exit':
            print('Thanks for choosing Password Generator')
            break

