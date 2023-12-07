#! /usr/bin/python

import sys

def parse_line(line):
    id, games = line.split(":")
    id = int(id.split()[1])
    reveals = games.split(';')
    reveals = [x.split(",") for x in reveals]
    for i in range(len(reveals)):
        reveals[i] = [x.strip().split() for x in reveals[i]]
        for pair in reveals[i]:
            pair[0] = int(pair[0])
    return (id, reveals)


def fewest_set(game):
    """
    Given list representing a game, with several reveals of sets of dice from the same bag,
    Determine the minimum count of cubes required per each color for the game.
    Multiply the resulting counts.

    Usage examples:
    >>> fewest_set([[[3, 'blue'], [4, 'red']], [[1, 'red'], [2, 'green'], [6, 'blue']], [[2, 'green']]])
    48
    >>> fewest_set([[[1, 'blue'], [2, 'green']], [[3, 'green'], [4, 'blue'], [1, 'red']], [[1, 'green'], [1, 'blue']]])
    12
    >>> fewest_set([[[8, 'green'], [6, 'blue'], [20, 'red']], [[5, 'blue'], [4, 'red'], [13, 'green']], [[5, 'green'], [1, 'red']]])
    1560
    >>> fewest_set([[[1, 'green'], [3, 'red'], [6, 'blue']], [[3, 'green'], [6, 'red']], [[3, 'green'], [15, 'blue'], [14, 'red']]])
    630
    >>> fewest_set([[[6, 'red'], [1, 'blue'], [3, 'green']], [[2, 'blue'], [1, 'red'], [2, 'green']]])
    36
    """
    color_counts = dict()
    for reveal in game:
        for color_reveal in reveal:
            if color_reveal[1] in color_counts:
                if color_reveal[0] > color_counts[color_reveal[1]]:
                    color_counts[color_reveal[1]] = color_reveal[0]
            else:
                color_counts[color_reveal[1]] = color_reveal[0]
    power = 1
    for x in color_counts.values():
        power *= x
    return power


def is_possible(reveal):
    """
    Determine if a particular reveal of cubes is possible, given the cube color counts.
    """
    possible_counts = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    for color_reveal in reveal:
        if color_reveal[0] > possible_counts[color_reveal[1]]:
            # One color reveal is above the bounds
            return False
    return True


def cube(games):
    """
    Given lines representing a game, and a count of colored dice,
    Determine which games are possible and sum their IDs.
    Also determine the min count of cubes per color, and sum the product of those counts.

    Usage examples:
    >>> cube([\
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",\
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",\
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",\
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",\
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"\
    ])
    (8, 2286)
    """
    possible_sum = 0
    power_sum = 0
    for game in games:
        id, reveals = parse_line(game)
        good_game = True
        for reveal in reveals:
            if not is_possible(reveal):
                good_game = False
                break
        if good_game:
            possible_sum += id
        power = fewest_set(reveals)
        power_sum += power
        #print(f"Sum of possible game IDs after game {id}: {possible_sum}")
        #print(f"Dice Power of game {id}: {power}")
    return (possible_sum, power_sum)


def test():
    # A more in-depth test harness for enhanced debugging.
    from json import load
    f = open("test_data.json", "r")
    contents = load(f)
    f.close()
    for item in contents:
        pass
    print("All tests passed.")


if __name__ == '__main__':   
    if sys.argv[1] == '-t':
        test()
    else:
        f = open(sys.argv[1], "r")
        contents = f.readlines()
        f.close() 
        possible_sum, power_sum = cube(contents)
        
        print(f"Sum of IDs of possible games: {possible_sum}")
        print(f"Sum of powers of min die counts of games: {power_sum}")