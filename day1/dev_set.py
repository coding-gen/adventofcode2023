#! /usr/bin/python

import sys
from random import randint 

f = open(sys.argv[1], "r")
contents = f.readlines()
f.close() 

ff = open('dev_data.txt', 'w')
for line in contents:
    # 10%
    if randint(0, 9) == 5:
        ff.write(line)
ff.close()