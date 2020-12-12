import copy
import itertools
from functools import cache
from pprint import pprint as pp

floor, empty_chair, occupied_chair, = ".", "L", "#"

SURROUND_COORDS = list(itertools.product(range(-1, 2), range(-1, 2)))
SURROUND_COORDS.remove((0, 0))


@cache
def coords(i):
    s = list(itertools.product(range(i - 1, i + 2), repeat=2))
    s.remove((0, 0))
    return s


def search_paths(i, limit):
    rad = 1
    while rad < limit:
        for x, y in coords(i):
            yield x*rad, y*rad
        rad += 1


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

        for i, j in itertools.product(range(0, rows), range(0, cols)):
            if previous[i][j] == floor:
                continue

            occupied = 0
            for a, b in coords(0, 1):
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


# def search_paths(w, h):
#     # to the left
#
#     # to the right
#     for y in range(0, h):
#         print('right')
#         yield ((x, y) for x in range(w))
#
#     for x in range(0, w):
#         print('down')
#         yield ((x, y) for y in range(h))
#
#     # down and to the right
#     for x0 in range(-h + 1, w):
#         print('down right')
#         yield ((x0 + y, y) for y in range(max(0, -x0), min(h, w - x0)))
#         # down and to the left
#     for x0 in range(0, w + h):
#         print('down left')
#         yield ((x0 - y, y) for y in range(max(0, x0 - w + 1), min(h, x0 + 1)))

t = """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""

test = [list(x) for x in t.splitlines()]

def part_two():
    print('Part two')
    puzzle = read()
    w, h = len(puzzle), len(puzzle[0])
    seats = {
        (x, y): {(x, y)} for x, y in itertools.product(range(w), range(h)) if puzzle[x][y] != floor
    }

    print(seats)

@cache
def valid(x, y, dx, dy, rows, cols):
    return x+dx not in range(rows) or y+dy not in range(cols)

if __name__ == '__main__':
    # part_one()
    part_two()
    rows, cols = len(test), len(test[0])

    r, c = 3, 3
    # wip multiplier based search paths
    for x, y in search_paths(0, max(rows, cols)):
        print(x, y)
        # if r+x not in range(rows) or c+y not in range(cols):
        #     continue
        if not valid(r, c, x, y, rows, cols):
            continue
        print(test[r+x][c+y])

