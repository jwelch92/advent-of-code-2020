from typing import List
import bisect


def solve_one(arrival, schedule):
    bus_id = 0
    low = arrival
    for bus in sorted(schedule):
        q, rem = divmod(arrival, bus)

        d = abs(arrival - ((q + 1) * bus))
        if d < low:
            low = d
            bus_id = bus

    return low * bus_id


def solve_two(puzzle):
    pass


def parse(p):
    return int(p[0]), [int(x) for x in p[1].split(",") if x != "x"]


def read() -> List[str]:
    with open("input.txt") as f:
        return f.read().splitlines()


def part_one():
    print('Part one')
    target, schedule = parse(read())
    solve_one(target, schedule)


def part_two():
    print('Part two')


if __name__ == '__main__':
    part_one()
    part_two()
