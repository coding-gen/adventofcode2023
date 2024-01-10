#! /usr/bin/python

import sys


def parse_input(paper):
    construction = {}
    i = 0
    while i < len(paper):
        if len(paper[i]) < 2:
            # empty row
            i += 1
        if paper[i][:5] == 'seeds':
            line = paper[i].split(':')[1].strip().split()
            seed_counter = 0
            while seed_counter < len(line):
                seed_id = int(line[seed_counter])
                seed_range = int(line[seed_counter + 1])
                construction['seeds'] = construction.get('seeds', []) + [{'id': seed_id, 'range': seed_range}]
                seed_counter += 2
        elif not paper[i][0].isnumeric(): 
            mappings = []
            name = paper[i].split()[0]
            i += 1
            while i < len(paper) and paper[i][0].isnumeric():
                line = paper[i].split()
                mappings.append([int(item) for item in line])
                i += 1
            construction[name] = mappings
        i += 1
    return construction


def calculate_winning_amount(matches):
    length = len(matches)
    if length > 0:
        return 2 ** (length -1)
    return 0


def count_scratchcards(d):
    return sum(d.values())


def controller(schematic):
    """
    Part 1:
 

    part1 result: 13
    part2 result: 30
    """
    part1_sum = 0
    card_counts = {}

    return (1, 2)


if __name__ == '__main__':   
    f = open(sys.argv[1], "r")
    contents = f.readlines()
    f.close() 
    part1, part2 = controller(contents)
    print(f"Winning sum of power of 2: {part1}")
    print(f"Winning count of scratchcards: {part2}")