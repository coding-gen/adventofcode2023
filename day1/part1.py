#! /usr/bin/python

import sys
import re

def sum_digits(lines):
    """Locate first and last digits in a string, they are the digits of a number
    Compute the sum of such a number for each line in the input.

    Usage examples:
    >>> sum_digits(['1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet'])
    142
    """
    sum = 0
    for line in lines:
        digits = re.findall("([0-9])", line)
        if len(digits) > 0:
            sum += int(digits[0] + digits[-1])
    return sum


if __name__ == '__main__':
    f = open(sys.argv[1], "r")
    contents = f.readlines()
    f.close() 
    print(sum_digits(contents))
