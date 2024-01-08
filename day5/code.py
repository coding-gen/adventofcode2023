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


def unpack_seed_ranges(seeds):
    """
    Unpack all the seeds in the given range.

    Usage example:
    >>> unpack_seed_ranges([{'id': 79, 'range': 14}, {'id': 55, 'range': 13}])
    [[79], [80], [81], [82], [83], [84], [85], [86], [87], [88], [89], [90], [91], [92], [55], [56], [57], [58], [59], [60], [61], [62], [63], [64], [65], [66], [67]]
    """
    full_seeds = []
    for seed in seeds:
        for i in range(seed['range']):
            full_seeds.append([seed['id'] + i])
    return full_seeds


def walk_map(histories, table, conversion_name):
    return [[convert(history[0], table[conversion_name])] + history for history in histories]


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
    part2 result: 46
    """

    table = parse_input(almanac)
    
    # I chose to track the history of each seed's path through the mappings.
    # In a practical scenario where you'd actually plant the seeds, 
    # you'd need info on each of the planting conditions. 
    # Here we have already calculated it per seed, so we may as well keep it for later use.

    """
    for each seed
    convert all the way to location
    if smaller than current location, swap it out
    high cpu usage
    much lower memory usage.
    """
    # next seed
    # convert to location
    # location comparison
    full_seeds = unpack_seed_ranges(table['seeds'])
    soils = walk_map(full_seeds, table, 'seed-to-soil')
    fertilizers = walk_map(soils, table, 'soil-to-fertilizer')
    waters = walk_map(fertilizers, table, 'fertilizer-to-water')
    lights = walk_map(waters, table, 'water-to-light')
    temperatures = walk_map(lights, table, 'light-to-temperature')
    humidities = walk_map(temperatures, table, 'temperature-to-humidity')
    mapping_paths = walk_map(humidities, table, 'humidity-to-location')

    mapping_paths.sort()
    return (mapping_paths[0][0])


if __name__ == '__main__':   
    f = open(sys.argv[1], "r")
    contents = f.readlines()
    f.close() 
    part2 = controller(contents)
    print(f"lowest location: {part2}")
