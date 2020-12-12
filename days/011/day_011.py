import copy
import itertools
from pprint import pprint as pp

floor, empty_chair, occupied_chair, = ".", "L", "#"

SURROUND_COORDS = list(itertools.product(range(-1, 2), range(-1, 2)))
SURROUND_COORDS.remove((0, 0))

sample_final_raw = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""

sample_final = [list(x) for x in sample_final_raw.splitlines()]


def read():
    with open('input.txt') as f:
        data = f.read().splitlines()
    return [list(x) for x in data]


def count_total_occupied(boat):
    return sum(x.count(occupied_chair) for x in boat)


def solve_one(puzzle_input):
    iterations = 0
    working = copy.deepcopy(puzzle_input)
    previous = copy.deepcopy(puzzle_input)
    while True:
        rows = len(working)
        cols = len(working[0])

        for i in range(0, rows):
            for j in range(0, cols):
                if previous[i][j] == floor:
                    continue

                occupied = 0
                for a, b in SURROUND_COORDS:
                    row = i + a
                    col = j + b
                    if (row >= 0 and col >= 0) and (row < rows and col < cols):
                        occupied += int(previous[row][col] == occupied_chair)
                if previous[i][j] == empty_chair and occupied == 0:
                    working[i][j] = occupied_chair
                    continue
                if previous[i][j] == occupied_chair and occupied >= 4:
                    working[i][j] = empty_chair
                    continue

        if working == previous:
            break
        iterations += 1
        previous = copy.deepcopy(working)

    return count_total_occupied(working), working


def part_one():
    print('Part one')
    puzzle = read()
    ans, _ = solve_one(puzzle)
    print("ans", ans)


def part_two():
    print('Part two')


if __name__ == '__main__':
    part_one()
    part_two()
