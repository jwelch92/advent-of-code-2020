import copy
import itertools
from pprint import pprint as pp

with open('input.txt') as f:
    data = f.read().splitlines()

floor, ec, oc, = ".", "L", "#"

test_raw = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

test = [list(x) for x in test_raw.splitlines()]

around = list(itertools.product(range(-1, 2), range(-1, 2)))
around.remove((0, 0))
print(around)

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


# print(a, b, test[a][b])

def count_total_occupied(boat):
    return sum(x.count(oc) for x in boat)


print(data)
puzzle_input = [list(x) for x in data]
print(puzzle_input)

iterations = 0
working = copy.deepcopy(puzzle_input)
previous = copy.deepcopy(puzzle_input)

print(working)

print(previous)

while True:
    print("Starting round", iterations)
    rows = len(working)
    cols = len(working[0])

    for i in range(0, rows):
        for j in range(0, cols):
            if previous[i][j] == floor:
                continue

            occupied = 0
            for a, b in around:
                row = i + a
                col = j + b
                if (row >= 0 and col >= 0) and (row < rows and col < cols):
                    # print(row, col, previous[row][col])
                    occupied += int(previous[row][col] == oc)
            # print(occupied)
            if previous[i][j] == ec and occupied == 0:
                working[i][j] = oc
                continue
            if previous[i][j] == oc and occupied >= 4:
                working[i][j] = ec
                continue

    iterations += 1
    if working == previous:
        pp(working)
        pp(previous)
        break
    print("not the same, copying")
    previous = copy.deepcopy(working)

print(iterations)
pp(previous)

print(count_total_occupied(working))

# for a, b in zip(working, sample_final):
#     print(a, b)
#     assert a == b
#
# # assert iterations == 5
# assert count_total_occupied(working) == 37
# assert sample_final == previous
# def part_one():
#     print('Part one')
#
#
# def part_two():
#     print('Part two')
#     # my answer from part one
#
#
# if __name__ == '__main__':
#     part_one()
#     part_two()
