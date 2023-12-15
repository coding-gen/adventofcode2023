#! /usr/bin/python

import sys


def get_part_length(line, start):
    """
    Determine how many digits there are in a row.
    """
    i = 0
    while i <= 4 and (start + i) < len(line):
        if not line[start + i].isnumeric():
            return i
        i += 1
    return 4 # number sequences are less than 3, this should never be hit.


def calculate_schematic_sums(schematic):
    """
    Given lines representing an engine schematic, 
    locate all the part numbers, which are numerical sequences touching special chars.
    Additionally if that special char is a star, then the part is a gear.
    Sum all part numbers, and sum the ratio of all gears.

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

    result: (4361, 467835)
    """
    schematic = [[character for character in line.strip()] for line in schematic]
    height = len(schematic)
    width = len(schematic[0])

    special_chars = '@#$%&*/=+-'
    parts = []
    gears = {}
    for i, line in enumerate(schematic):
        j = 0
        while j < len(line):
            if line[j].isnumeric():
                # This is a part. Locate the start, end of the part number
                part_length = get_part_length(line, j)
                
                # Check the surrounding squares of the part for special chars
                is_part = False # for faster escape if we find a special char early.
                for row_id in range(i-1, i+2):
                    for col_id in range(j-1, j + part_length + 1):
                        part = ''.join(line[j : j + part_length])

                        # Within the matrix width
                        if col_id >= 0 and col_id < width:
                            if row_id == i:
                                # On the part row, only check the ends.
                                if col_id < j or col_id >= j + part_length:
                                    if schematic[row_id][col_id] in special_chars:
                                        if schematic[row_id][col_id] == '*': # gear check
                                            gears[(row_id, col_id)] = gears.get((row_id, col_id), []) + [part]
                                        parts.append(part)
                                        is_part = True

                            # Within the matrix height
                            elif row_id >= 0 and row_id < height:
                                    if schematic[row_id][col_id] in special_chars:
                                        if schematic[row_id][col_id] == '*': # gear check
                                            gears[(row_id, col_id)] = gears.get((row_id, col_id), []) + [part]
                                        parts.append(part)
                                        is_part = True
                        if is_part: break
                    if is_part: break
                j += part_length # We know the next char is not numeric, skip it.
            else: 
                j += 1
    sum = 0
    for x in parts:
        sum += int(x)
    
    gear_sum = 0
    for gear_parts in gears.values():
        if len(gear_parts) == 2:
            gear_sum += int(gear_parts[0]) * int(gear_parts[1])
    return (sum, gear_sum)


if __name__ == '__main__':   
    f = open(sys.argv[1], "r")
    contents = f.readlines()
    f.close() 
    part_sum, gear_sum = calculate_schematic_sums(contents)
    print(f"Parts sum: {part_sum}")
    print(f"Gear ratios sum: {gear_sum}")

