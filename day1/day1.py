#! /usr/bin/python

import re

f = open("input-day1.txt", "r")

contents = f.readlines()
f.close() 
sum = 0
for line in contents:
    digits = re.findall("([0-9])", line)
    if len(digits) > 0:
        sum += int(digits[0] + digits[len(digits)-1])

print(sum)
