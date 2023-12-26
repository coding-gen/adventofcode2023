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
            construction['seeds'] = [int(seed) for seed in line]
        elif not paper[i][0].isnumeric(): 
            mappings = []
            name = paper[i].split()[0]
            i += 1
            while i<len(paper) and paper[i][0].isnumeric():
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


def controller(almanac):
    """
    Part 1:
    Use the given mapping of various seed growing conditions to find the nearest location for the given seeds.
    Two ways to accomplish:
    Build giant list or dict with each calculated mapping. Look up the seeds in the maps.
        Benefit: fast lookup, low CPU, easy to think about.
        Cost: building giant map tables for only a few seeds.
        Here: Very large tables, very few seeds
    Automatically handle the calculations that convert through ranges over mappings.
        Benefit: not build huge tables. Feels more clever.
        Cost: easy to do manually creating if statements. 
            Harder to get machine to automatically pull ranges and create calculations.
            Must calculate all ranges and lookup, for each seed.
            More CPU hungry.
            Here: small set of seeds, large tables
    Option2.

    Usage example:
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15

        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4

        water-to-light map:
        88 18 7
        18 25 70

        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13

        temperature-to-humidity map:
        0 69 1
        1 0 69

        humidity-to-location map:
        60 56 37
        56 93 4

    part1 result: 35
    part2 result: 
    """

    part1_sum = 0
    part2_calculation = 0

    table = parse_input(almanac)
    for mapping in table.items():
        print (mapping)

    return (part1_sum, part2_calculation)


if __name__ == '__main__':   
    f = open(sys.argv[1], "r")
    contents = f.readlines()
    f.close() 
    part1, part2 = controller(contents)
    print(f"Part1 sum: {part1}")
    print(f"Part2 calculation: {part2}")