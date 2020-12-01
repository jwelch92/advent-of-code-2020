import itertools
import math

from days.lib import inputs


def search(size: int):
    data = inputs.parse_input("input.txt", parse_int=True)
    print(data)
    for x in itertools.combinations(data, size):
        if sum(x) == 2020:
            print('Found solution')
            print(math.prod(x))
            break


def part_one():
    print('Part one')
    search(2)


def part_two():
    print('Part two')
    search(3)


if __name__ == '__main__':
    part_one()
    part_two()
