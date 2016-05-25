#!/usr/bin/env python

"""  
Super awesome script  
Asks the user for a number:  
 - If the number is less or equal to 100, it returns it to the power of itself
 - else, it returns the number squared
"""


import argparse

__version__ = '0.3'


def calculation(number):
    if number > 100:
        return number**2
    else:
        return number**number


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', required=True, type=int,
                        help='number to perform calculation')
    values = parser.parse_args()
    user_number = values.number
    calculation_result = calculation(user_number)
    print(calculation_result)


#input validation handled by argparse, not done within the script itself
