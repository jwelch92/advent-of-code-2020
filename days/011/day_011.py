import copy
import itertools
from functools import cache

floor, empty_chair, occupied_chair, = ".", "L", "#"


@cache
def surrounding_coords(i):
    s = list(itertools.product(range(i - 1, i + 2), repeat=2))
    s.remove((0, 0))
    return s


mods = surrounding_coords(0)

cardinals = {
    point: s for point, s in zip(surrounding_coords(0), ["NW", "N", "NE", "W", "E", "SW", "S", "SE"])
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
            for row, col in list(tuple(map(sum, zip((i, j), mod))) for mod in mods):
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


def solve_two(puzzle_input, round_limit=-1):
    working = copy.deepcopy(puzzle_input)
    previous = copy.deepcopy(puzzle_input)
    rows = len(working)
    cols = len(working[0])
    valid_row = make_within(rows)
    valid_col = make_within(cols)
    num_rounds = 0
    while True:
        if round_limit != -1 and num_rounds == round_limit:
            print("LIMIT REACHED, EXITING...")
            break

        for i, j in itertools.product(range(0, rows), range(0, cols)):
            if previous[i][j] == floor:
                continue
            occupied = 0
            moves = list(tuple(map(sum, zip((i, j), mod))) for mod in mods)
            for index, (x, y) in enumerate(moves):
                found = False

                while not found:
                    if not valid_row(x) or not valid_col(y):
                        found = True
                    elif previous[x][y] == floor:
                        # expand search additively by the coords
                        x += mods[index][0]
                        y += mods[index][1]
                    elif previous[x][y] == empty_chair or previous[x][y] == occupied_chair:
                        occupied += int(previous[x][y] == occupied_chair)
                        found = True

            if previous[i][j] == empty_chair and occupied == 0:
                working[i][j] = occupied_chair
                continue
            if previous[i][j] == occupied_chair and occupied >= 5:
                working[i][j] = empty_chair
                continue

        if working == previous:
            break

        num_rounds += 1
        previous = copy.deepcopy(working)

    return count_total_occupied(working), working


def part_one():
    # super slow
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
    # even slower
    print('Part two')
    puzzle = read()
    ans, _ = solve_two(puzzle)
    print("ans", ans)


@cache
def valid(x, y, dx, dy, rows, cols):
    return x + dx not in range(rows) or y + dy not in range(cols)


if __name__ == '__main__':
    part_one()
    part_two()
