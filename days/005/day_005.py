import collections
from typing import List
from functools import cache


def read() -> List[str]:
    with open('input.txt') as f:
        return [x.strip() for x in f.readlines()]


@cache
def search(code: str, lower: int, upper: int) -> int:
    for c in code:
        mid = (lower + upper) >> 1
        if c in ("B", "R"):
            lower = mid + 1
        else:
            upper = mid
    return lower


def get_col(boarding_pass: str) -> int:
    return search(boarding_pass[7:10], 0, 7)


def get_row(boarding_pass: str) -> int:
    return search(boarding_pass[0:7], 0, 127)


def get_seat_id(boarding_pass: str) -> int:
    print(boarding_pass)
    row = get_row(boarding_pass)
    col = get_col(boarding_pass)

    return (row * 8) + col


def missing_elements(elems):
    start, end = elems[0], elems[-1]
    return sorted(set(range(start, end + 1)).difference(elems))


def part_one():
    print('Part one')
    ids = [get_seat_id(x) for x in read()]
    print(max(ids))


def part_two():
    print('Part two')
    ids = [get_seat_id(x) for x in read()]
    print(missing_elements(sorted(ids)))

    c = collections.Counter(ids)
    print(c)


if __name__ == '__main__':
    part_one()
    part_two()
