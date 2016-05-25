#!/usr/bin/env python

"""  
Super awesome script  
Asks the user for a number:  
 - If the number is less or equal to 100, it returns it to the power of itself
 - else, it returns the number squared
"""


import argparse

__version__ = '0.2'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', required=True, type=int,
                        help='number to perform calculation')
    values = parser.parse_args()
    user_number = values.number
    if user_number > 100:
        print(user_number**2)
    else:
        print(user_number**user_number)
