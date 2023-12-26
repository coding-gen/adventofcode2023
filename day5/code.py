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


def convert(seed, conversion_list):
    """
    Convert an item index using the given mapping:
    [destination_range_start, source_range_start, range_length]

    Usage examples:
    >>> convert(79, [[50, 98, 2], [52, 50, 48]])
    81
    >>> convert(14, [[50, 98, 2], [52, 50, 48]])
    14
    >>> convert(55, [[50, 98, 2], [52, 50, 48]])
    57
    >>> convert(13, [[50, 98, 2], [52, 50, 48]])
    13
    """
    for dest, source, range_length in conversion_list:
        if seed >= source and seed <= source + range_length:
            return dest + seed - source
    return seed


def walk_map(histories, table, conversion_name):
    return [[convert(history[0], table[conversion_name])] + history for history in histories]


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
    # TODO could change input parsing to list of tuples instead of dict, and walk its conversions in order of index. 
    # Here we have to call them by key name.
    # It might end up being useful to see the whole path per seed, so we'll track it.
    soils = [[convert(seed, table['seed-to-soil']), seed] for seed in table['seeds']]
    fertilizers = walk_map(soils, table, 'soil-to-fertilizer')
    waters = walk_map(fertilizers, table, 'fertilizer-to-water')
    lights = walk_map(waters, table, 'water-to-light')
    temperatures = walk_map(lights, table, 'light-to-temperature')
    humidities = walk_map(temperatures, table, 'temperature-to-humidity')
    mapping_paths = walk_map(humidities, table, 'humidity-to-location')

    # By prepending the seed's planting conditions history with each new element in walk_map(), 
    # it allows us to simply sort at the outermost list level, to get the lowest location per seed.
    mapping_paths.sort()
    print(f"lowest location: {mapping_paths[0][0]}")

    """
    for seed in table['seeds']:
        converted.append(convert(seed, table['seed-to-soil']))
        print(f"the conversion: from {seed} to {convert(seed, table['seed-to-soil'])}")
    """


    return (part1_sum, part2_calculation)


if __name__ == '__main__':   
    f = open(sys.argv[1], "r")
    contents = f.readlines()
    f.close() 
    part1, part2 = controller(contents)
    print(f"Part1 sum: {part1}")
    print(f"Part2 calculation: {part2}")