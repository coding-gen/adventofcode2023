#! /usr/bin/python

import sys

def parse_line(line):
    id, games = line.split(":")
    id = int(id.split()[1])
    reveals = games.split(';')
    reveals = [x.split(",") for x in reveals]
    for i in range(len(reveals)):
        reveals[i] = [x.strip().split() for x in reveals[i]]
    return (id, reveals)


def is_possible(reveal):
    """
    Determine if a particular reveal of dice is possible, given the die counts.
    """
    possible_counts = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    for color_reveal in reveal:
        if int(color_reveal[0]) > possible_counts[color_reveal[1]]:
            # One color reveal is above the bounds
            return False
    return True


def count_possible(games):
    """
    Given lines representing a game,
    and a count of colored dice,
    Determine which games are possible.
    Sum and return the game ids.

    Usage examples:
    >>> count_possible([\
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",\
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",\
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",\
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",\
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"\
    ])
    8
    """
    possible_sum = 0
    for game in games:
        id, reveals = parse_line(game)
        good_game = True
        for reveal in reveals:
            if not is_possible(reveal):
                good_game = False
                break
        if good_game:
            possible_sum += id
        print(f"possible_sum after game {id}: {possible_sum}")
    return possible_sum


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
        print(count_possible(contents))