#! /usr/bin/python

import sys
import re


def locate_first_last(line):
    """Locate first and last numbers in a string whether digits or spelled out.

    Usage examples:
    >>> locate_first_last('two1nine')
    ('2', '9')
    >>> locate_first_last('eightwothree')
    ('8', '3')
    >>> locate_first_last('abcone2threexyz')
    ('1', '3')
    >>> locate_first_last('xtwone3four')
    ('2', '4')
    >>> locate_first_last('4nineeightseven2')
    ('4', '2')
    >>> locate_first_last('zoneight234')
    ('1', '4')
    >>> locate_first_last('7pqrstsixteen')
    ('7', '6')
    >>> locate_first_last('szcspm5sixtwovtrmvrthreefour7oneightqqj')
    ('5', '8')
    >>> locate_first_last('83threethreeeightninethree')
    ('8', '3')
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
    first = re.findall(r"([0-9]|one|two|three|four|five|eight|six|seven|eight|nine).*", line)[0]
    last = re.findall(r".*([0-9]|one|two|three|four|five|eight|six|seven|eight|nine)", line)[0]
    if first in d:
        first = d[first]
    if last in d:
        last = d[last]
    return (first, last)



def sum_digits(lines):
    """Compute the sum for each line in the input.

    Usage examples:
    >>> sum_digits(['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen'])
    281
    """
    sum = 0
    for line in lines:
        first, last = locate_first_last(line.lower())
        sum += int(first + last)

    return sum


def test_locate_first_last():
    # A more in-depth test harness for enhanced debugging.
    from json import load
    f = open("test_data.json", "r")
    contents = load(f)
    f.close()
    for item in contents:
        result = locate_first_last(item["input"])
        assert (item["output1"], item["output2"]) == result, \
            f"Test Failure on entry {item['input']}: expected {item['output1'], item['output2']} but received: {result}"
    print("All tests passed.")

if __name__ == '__main__':   
    if sys.argv[1] == '-t':
            test_locate_first_last()
    else:
        f = open(sys.argv[1], "r")
        contents = f.readlines()
        f.close() 
        print(sum_digits(contents))
    