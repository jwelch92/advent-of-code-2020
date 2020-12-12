import math
from typing import List, Tuple

import parse

pat = parse.compile("{direction}{distance}")


def read() -> List[str]:
    with open('input.txt') as f:
        return f.read().splitlines()


cardinals: Dict[int, str] = {
    0: "E",
    90: "S",
    180: "W",
    270: "N"
}


def solve_one(puzzle_input: List[str]) -> int:
    facing = 0
    x, y = 0, 0

    for line in puzzle_input:
        print(line)
        move = pat.parse(line)
        units = int(move["distance"])
        direction = move["direction"]

        if direction == "F":
            direction = cardinals[facing]

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

    return abs(x) + abs(y)


def solve_two(puzzle_input: List[str]) -> int:
    x, y = 0, 0
    # waypoint coords are RELATIVE to the ship
    wx, wy = 10, 1

    for line in puzzle_input:
        print(line)
        move = pat.parse(line)
        units = int(move["distance"])
        direction = move["direction"]
        # F translate ship N times towards waypoint
        if direction == "F":
            y += units * wy
            x += units * wx

        if direction == "N":
            wy += units
        elif direction == "S":
            wy -= units
        elif direction == "E":
            wx += units
        elif direction == "W":
            wx -= units

        elif direction == "L":
            wx, wy = rotate((wx, wy), units)

        elif direction == "R":
            wx, wy = rotate((wx, wy), units * -1)

    return abs(x) + abs(y)


# rotate around 0,0 using M A T H
def rotate(point: Tuple[int, int], angle: int) -> Tuple[int, int]:
    ox, oy, = 0, 0
    px, py, = point
    angle = math.radians(angle)
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))


def part_one():
    print("Part one")
    d = read()
    ans = solve_one(d)
    print("ans", ans)


def part_two():
    print('Part two')
    print(rotate((10, 4), 180))
    d = read()
    ans = solve_two(d)
    print("ans", ans)


if __name__ == '__main__':
    part_one()
    part_two()
