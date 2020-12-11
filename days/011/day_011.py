import itertools
import copy
from pprint import pprint as pp

with open('input.txt') as f:
    data = f.read().splitlines()

floor, ec, oc, = ".", "L", "#"

test = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

test = [list(x) for x in test.splitlines()]

around = list(itertools.product(range(-1, 2), range(-1, 2)))
around.remove((0, 0))
print(around)

# print(a, b, test[a][b])



iterations = 0
previous = []
working = test
while True:
    print("Starting round", iterations)
    pp(working)
    rows = len(working)
    cols = len(working[0])

    for i in range(0, rows):
        for j in range(0, cols):
            print("checking", i, j)

            if working[i][j] == floor:
                continue

            occupied = 0
            for a, b in around:
                row = i + a
                col = j + b
                if (row >= 0 and col >= 0) and (row < rows and col < cols):
                    print(row, col, working[row][col])
                    occupied += int(working[row][col] == oc)
            print(occupied)
            if working[i][j] == ec and occupied == 0:
                working[i][j] = oc
                continue
            if working[i][j] == oc and occupied >= 4:
                working[i][j] = ec
                continue

    iterations += 1
    if working == previous:
        pp(working)
        pp(previous)
        break
    print("not the same, copying")
    previous = copy.deepcopy(working)


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
