#!/usr/bin/env python

"""  
Super awesome script  
Asks the user for a number:  
 - If the number is less or equal to 100, it returns the 1st tetration of the number (power of itself)
 - else, it returns the number squared
"""

__version__ = '0.1'

if __name__ == '__main__':

    while 1:
        user_number = input('Choose a number:\n')
        if user_number.isdigit():
            user_number = int(user_number)
            break
        else:
            print('{} is not a valid number'.format(user_number))

    if user_number > 100:
        print(user_number**2)
    else:
        print(user_number**user_number)
