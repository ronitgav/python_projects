# -*- coding: utf-8 -*-

"""
Write a function that takes an ordered list of numbers (a list where the
elements are in order from smallest to largest) and another number. The
function decides whether or not the given number is inside the list and
returns (then prints) an appropriate boolean.

Extras:

=> Use binary search.
"""

def ele_search(l, num):
    list_to_search = sorted([int(i) for i in l])
    if len(list_to_search) == 1:
        if num in list_to_search and len(list_to_search) == 1:
            return True
        else:
             return False
    else:
        if num < list_to_search[int(len(list_to_search))-1]:
            return ele_search(list_to_search[:len(list_to_search)/2], num)
        else:
            return ele_search(list_to_search[len(list_to_search)/2:], num)


if __name__ == '__main__':
    check = True

    while True:
        cmd = raw_input('Enter a list of numbers: ')
        if cmd == 'exit':
            break
        else:
            cmd = cmd.split(' ')
            num = int(raw_input('Enter a number to find in the above list: '))
            if ele_search(cmd, num) == True:
                print('Yes, %d exists' % num)
            else:
                print('Sorry, %d not found' % num)
