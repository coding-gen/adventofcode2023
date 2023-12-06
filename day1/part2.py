#! /usr/bin/python

import sys
import re

def sum_digits(lines):
    """Locate first and last numbers in a string whether digits or spelled out. 
    They are the digits of a number.
    Compute the sum of such a number for each line in the input.

    Usage examples:
    >>> sum_digits(['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen', 'szcspm5sixtwoefour7oneightqqj', '83threethreeeightninethree'])
    422
    """
    d = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    sum = 0
    for line in lines:
        first = re.findall(r"([0-9]|one|two|three|four|five|eight|six|seven|eight|nine).*", line)[0]
        last = re.findall(r".*([0-9]|one|two|three|four|five|eight|six|seven|eight|nine)", line)[0]
        if first in d:
            first = d[first]
        if last in d:
            last = d[last]
        sum += int(first + last)
    return sum


if __name__ == '__main__':
    f = open(sys.argv[1], "r")
    contents = f.readlines()
    f.close() 
    print(sum_digits(contents))
