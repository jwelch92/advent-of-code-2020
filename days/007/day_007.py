from collections import defaultdict
from functools import reduce
from typing import Dict, Set
from typing import List

import parse


def read() -> List[str]:
    with open('input.txt') as f:
        return [x.strip() for x in f.readlines()]


shiny_gold = "shiny gold"

Bags = Dict[str, Dict[str, int]]


def parse_input(puzzle_input) -> Bags:
    bags = defaultdict(dict)

    for line in puzzle_input:
        color, raw_contains = line.split(" bags contain ")
        for c in parse.findall("{count:d} {color} bag", raw_contains):
            bags[color][c["color"]] = c["count"]
    return bags


def solve_one(puzzle_input: List[str]) -> int:
    bags = parse_input(puzzle_input)
    return len(contains_bag(bags, shiny_gold))


# ugh I didn't get here on my own. Shout out reddit for teaching me cool python tricks
def contains_bag(bags: Bags, color: str) -> Set[str]:
    parents = set(parent_name for (parent_name, held) in bags.items() if color in held)
    return reduce(lambda a, b: a.union(contains_bag(bags, b)), parents, parents)


def search(bags: Bags, bag: str) -> int:
    count = 1
    for s in bags[bag]:
        m = bags[bag][s]
        count += m * search(bags, s)
    return count


def solve_two(puzzle_input: List[str]) -> int:
    bags = parse_input(puzzle_input)
    ans = search(bags, shiny_gold) - 1
    return ans


def part_one():
    print('Part one')
    print(solve_one(read()))


def part_two():
    print('Part two')
    ans = solve_two(read())
    print("ans", ans)


if __name__ == '__main__':
    part_one()
    part_two()
