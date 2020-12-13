from typing import List
from functools import reduce


def solve_one(arrival, schedule):
    bus_id = 0
    low = arrival
    for bus in sorted(schedule):
        q = arrival // bus
        d = abs(arrival - ((q + 1) * bus))
        if d < low:
            low = d
            bus_id = bus

    return low * bus_id


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def solve_two(puzzle):
    pass
    # part two is just CRT. There's online solvers or some pyton impl like the rostta stone one above.
    # TODO figure out how plumb my data into one of these lol


def parse_for_two(p):
    return p[1].split(",")


def parse_for_one(p):
    return int(p[0]), [int(x) for x in p[1].split(",") if x != "x"]


def read() -> List[str]:
    with open("input.txt") as f:
        return f.read().splitlines()


def part_one():
    print('Part one')
    target, schedule = parse_for_one(read())
    print(solve_one(target, schedule))


def part_two():
    print('Part two')
    puzzle = parse_for_two(read())
    print(solve_two(puzzle))


if __name__ == '__main__':
    part_one()
    part_two()
