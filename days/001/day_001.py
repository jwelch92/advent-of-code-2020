import itertools
import math


def parse_input(file: str, parse_int: bool = False):
    with open(file) as f:
        return [int(x.strip()) if parse_int else x.strip() for x in f.readlines()]


def search(size: int) -> int:
    data = parse_input("input.txt", parse_int=True)
    for x in itertools.combinations(data, size):
        if sum(x) == 2020:
            return math.prod(x)


def part_one():
    print('Part one')
    print(search(2))


def part_two():
    print('Part two')
    print(search(3))


if __name__ == '__main__':
    part_one()
    part_two()
