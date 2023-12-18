#! /usr/bin/python

import sys


def parse_input(line):
    card, number_lists = line.split(':')
    card_id = int(card.strip().split()[1])
    left, right = number_lists.strip().split('|')
    winning_numbers = left.strip().split()
    winning_numbers = [int(x) for x in winning_numbers]
    chosen_numbers = right.strip().split()
    chosen_numbers = [int(x) for x in chosen_numbers]
    return (card_id, winning_numbers, chosen_numbers)


def find_matches(winning_numbers, chosen_numbers):
    """
    Given two lists, find their intersection using mergesort.

    Usage examples:
    >>> find_matches([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])
    [17, 48, 83, 86]
    >>> find_matches([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19])
    [32, 61]
    >>> find_matches([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1])
    [1, 21]
    >>> find_matches([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83])
    [84]
    >>> find_matches([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36])
    []
    >>> find_matches([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11])
    []
    """
    winning_numbers.sort()
    chosen_numbers.sort()
    matches = []
    i = 0
    j = 0
    while i < len(winning_numbers) and j < len(chosen_numbers):
        if winning_numbers[i] == chosen_numbers[j]: 
            matches.append(winning_numbers[i])
            i += 1
            j += 1
        elif winning_numbers[i] > chosen_numbers[j]:
            j += 1
        else:
            i += 1
    return matches


def calculate_winning_amount(matches):
    length = len(matches)
    if length > 0:
        return 2 ** (length -1)
    return 0


def controller(schematic):
    """
    Count how many numbers are present in both lists.
    Calculate 2^(n-1) where n is the count.
    Sum the previous calculation over all cards.

    Usage example:
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

    result: 13
    """
    sum = 0
    for line in schematic:
        id, winning_numbers, chosen_numbers = parse_input(line)
        matches = find_matches(winning_numbers, chosen_numbers)
        sum += calculate_winning_amount(matches)
    return sum


if __name__ == '__main__':   
    f = open(sys.argv[1], "r")
    contents = f.readlines()
    f.close() 
    sum = controller(contents)
    print(f"Winning: {sum}")

