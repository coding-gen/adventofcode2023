#! /usr/bin/python

import sys


def calculate_winning_amount(schematic):
    """
    Count how many numbers are present in both lists.
    Calculate 2^(n-1) where n is the count.
    Sum the previous calculation over all cards.

    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

    result: 13
    """
    sum = 0
    return sum

if __name__ == '__main__':   
    f = open(sys.argv[1], "r")
    contents = f.readlines()
    f.close() 
    sum = calculate_winning_amount(contents)
    print(f"sum: {sum}")

