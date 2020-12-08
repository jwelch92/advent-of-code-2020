import pprint
from collections import defaultdict
from dataclasses import dataclass, field
from functools import reduce
from typing import List
import parse


# @dataclass(frozen=True)
# class Bag:
#     color: str = field(hash=True)
#     held: List["Bag"]
#
#     def contains(self, bag: "Bag") -> bool:
#         return any(x == bag for x in self.held)


def read() -> List[str]:
    with open('input.txt') as f:
        return [x.strip() for x in f.readlines()]


shiny_gold = "shiny gold"

def parse_input(puzzle_input):
    bags = defaultdict(list)

    for line in puzzle_input:
        color, raw_contains = line.split(" bags contain ")
        for c in parse.findall("{count:d} {color} bag", raw_contains):
            bags[color].extend([c["color"]] * c["count"])
    return bags

def solve_one(puzzle_input: List[str]) -> int:
    bags = parse_input(puzzle_input)
    return len(recur_bags(bags, shiny_gold))

# ugh I didn't get here on my own. Shoutout reddit for teaching me cool python tricks
def recur_bags(bags, color):
    parents = set(parent_name for (parent_name, held) in bags.items() if color in held)
    print(parents)
    return reduce(lambda a, b: a.union(recur_bags(bags, b)), parents, parents)





def part_one():
    print('Part one')
    print(solve_one(read()))


def part_two():
    print('Part two')
    bags = parse_input(read())




if __name__ == '__main__':
    part_one()
    part_two()
