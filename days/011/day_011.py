import itertools

with open('input.txt') as f:
    data = f.read().splitlines()

floor, ec, oc, = ".", "L", "#"


def neighbors(a, radius, rowNumber, columnNumber):
    return [[a[i][j] if i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0
             for j in range(columnNumber - 1 - radius, columnNumber + radius)]
            for i in range(rowNumber - 1 - radius, rowNumber + radius)]


print(data)

test = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14]
]


def nearby(a, x, y):
    rows = len(a)
    cols = len(a[0])
    # handle edges
    left = a[x][y - 1]
    right = a[x][y + 1]
    top = a[x - 1][y]
    down = a[x + 1][y]

    nw = [x - 1][y - 1]


i, j = 2, 2
n = list(itertools.product(range(i - 1, i + 2), range(j - 1, j + 2)))

for a, b in n:
    print(a, b, test[a][b])


# print(neighbors(test, 1, 1, 1))
# interesting approach here https://stackoverflow.com/questions/26363579/how-to-find-neighbors-of-a-2d-list-in-python/26363975


def part_one():
    print('Part one')


def part_two():
    print('Part two')
    # my answer from part one


if __name__ == '__main__':
    part_one()
    part_two()
