from itertools import combinations
from typing import List


def read() -> List[int]:
    with open('input.txt') as f:
        return [int(x.strip()) for x in f.readlines()]


def part_one():
    print('Part one')
    xmas = read()
    for i in range(25, len(xmas)):
        print(i)
        cur = xmas[i]
        c = combinations(xmas[i - 25:i], 2)

        for a, b in c:
            if a + b == cur:
                break
        else:
            print("did not find a pair for", cur)
            break


def part_two():
    print('Part two')
    # my answer from part one
    magic = 373803594

    xmas = read()
    count = len(xmas)
    for i in range(0, count):
        running = 0
        running_index = i
        while running < magic:
            running += xmas[running_index]
            running_index += 1
        if running == magic:
            r = xmas[i: running_index]
            print("ans", min(r) + max(r))
            break


if __name__ == '__main__':
    part_one()
    part_two()
