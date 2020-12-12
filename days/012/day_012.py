from dataclasses import dataclass
from itertools import combinations
from typing import List

import parse

pat = parse.compile("{direction}{distance}")


def read():
    with open('input.txt') as f:
        return f.read().splitlines()


#
# @dataclass
# class Ship:
#     facing: str
#     x: int
#     y: int
#

cardinals = {
    0: "E",
    90: "S",
    180: "W",
    270: "N"
}


def solve_one(puzzle_input):
    facing = 0
    x, y = 0, 0

    for line in puzzle_input:
        print(line)
        move = pat.parse(line)
        units = int(move["distance"])
        direction = move["direction"]

        if direction == "F":
            direction = cardinals[facing % 360]

        if direction == "N":
            y += units
        elif direction == "S":
            y -= units
        elif direction == "E":
            x += units
        elif direction == "W":
            x -= units
        elif direction == "L":
            facing = (facing - units) % 360
        elif direction == "R":
            facing = (facing + units) % 360

        print(x, y)
    print(x, y)

    return abs(x) + abs(y)


def part_one():
    print("Part one")
    d = read()
    ans = solve_one(d)
    print("ans", ans)


def part_two():
    print('Part two')


if __name__ == '__main__':
    part_one()
    part_two()
