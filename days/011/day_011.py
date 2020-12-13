import copy
import itertools
from functools import cache
from pprint import pprint as pp

floor, empty_chair, occupied_chair, = ".", "L", "#"


@cache
def coords(i):
    s = list(itertools.product(range(i - 1, i + 2), repeat=2))
    s.remove((0, 0))
    return s

cardinals = {
    point: s for point, s in zip(coords(0), ["NW", "N", "NE", "W", "E", "SW", "S", "SE"])
}


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
    rows = len(working)
    cols = len(working[0])
    while True:
        for i, j in itertools.product(range(0, rows), range(0, cols)):
            if previous[i][j] == floor:
                continue

            occupied = 0
            for a, b in coords(0):
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


def search_paths(x, y, limit):
    rad = 1
    while rad < limit:
        yield x * rad, y * rad
        rad += 1


def visualize(grid):
    for x in grid:
        print("".join(x))


def solve_two(puzzle, limit=-1):
    rows, cols = len(puzzle), len(puzzle[0])
    valid_row = make_within(rows)
    valid_col = make_within(cols)

    num_rounds = 0
    working = copy.deepcopy(puzzle)
    previous = copy.deepcopy(puzzle)

    while True:
        print("STARTING ROUND", num_rounds)
        # exit early for testing mid points
        if limit != -1 and num_rounds == limit:
            print("LIMIT REACHED, EXITING...")
            break
        for i, j in itertools.product(range(0, rows), range(0, cols)):
            if previous[i][j] == floor:
                continue
            print("Checking for seat", i, j)
            occupied = 0
            for bx, by in coords(0):
                print("searching towards", cardinals[(bx, by)])
                # todo optimize search path edges
                for a, b in search_paths(bx, by, max(rows-i, cols-j)):
                    # v[i][j] = "@"
                    row = i + a
                    col = j + b
                    if not valid_row(row) or not valid_col(col):
                        break

                    print("search deltas", a, b)
                    print("row, col", row, col)
                    print(previous[row][col])
                    if previous[row][col] in [empty_chair, occupied_chair]:
                        print("found a chair")
                        occupied += int(previous[row][col] == occupied_chair)
                        break
                visualize(working)

            print("occ", occupied)

            if previous[i][j] == empty_chair and occupied == 0:
                working[i][j] = occupied_chair
                continue
            if previous[i][j] == occupied_chair and occupied >= 5:
                print("EMPTYING CHAIR", i, j)
                working[i][j] = empty_chair

        if working == previous:
            break
        num_rounds += 1
        previous = copy.deepcopy(working)


    return count_total_occupied(working), working

    # for x, y in search_paths(0, max(rows, cols)):
    # print(x, y)
    # rx = r + x
    # cy = c + y
    #
    #
    # print(test[rx][cy])


def part_one():
    print('Part one')
    puzzle = read()
    ans, _ = solve_one(puzzle)
    print("ans", ans)


t = """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""

test = [list(x) for x in t.splitlines()]


def make_within(r):
    def within(x):
        return x in range(r)

    return within


def part_two():
    print('Part two')
    puzzle = read()
    w, h = len(puzzle), len(puzzle[0])
    # seats = {
    #     (x, y): {(x, y)} for x, y in itertools.product(range(w), range(h)) if puzzle[x][y] != floor
    # }

    # print(seats)


@cache
def valid(x, y, dx, dy, rows, cols):
    return x + dx not in range(rows) or y + dy not in range(cols)


if __name__ == '__main__':
    # part_one()
    part_two()
    # rows, cols = len(test), len(test[0])
    # valid_row = make_within(0, rows)
    # valid_col = make_within(0, cols)
    # r, c = 3, 3
    # # wip multiplier based search paths
    # for x, y in search_paths(0, max(rows, cols)):
    #     print(x, y)
    #     rx = r + x
    #     cy = c + y
    #
    #     if not valid_row(rx) or not valid_col(cy):
    #         continue
    #     print(test[rx][cy])
