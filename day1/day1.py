#! /usr/bin/python

import sys
import re

f = open(sys.argv[1], "r")

contents = f.readlines()
f.close() 
sum = 0
letter_numbers = [
        'one', '1',
        'two', '2',
        'three', '3',
        'four', '4',
        'five', '5',
        'six', '6',
        'seven', '7',
        'eight', '8',
        'nine', '9',
]
for line in contents:
    results = []

    digits = re.findall("([0-9]|one|two|three|four|five|six|seven|eight|nine)", line)
    for ln in letter_numbers:
        n = line.find(ln)
        if n > -1: 
            results.append((n, ln))
    results = sorted(results)
    print(f"results: {results}")
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
    if len(results) > 0:
        first = results[0][1]
        last = results[-1][1]
        if first in d:
            first = d[first]
        if last in d:
            last = d[last]
        sum += int(first + last)
        print(f"first: {first}\nlast: {last}\nsum: {sum}\nline: {line}")
    
print(sum)
