import itertools
from collections import defaultdict
from typing import List

import parse

# from threading import Lock

mask_pat = parse.compile("mask = {}")
set_pat = parse.compile("mem[{}] = {}")


def parser(input):
    print(input)
    instructions = []
    acc = [mask_pat.parse(input[0]).fixed[0]]
    for line in input[1:]:
        if "mask" in line:
            instructions.append(acc)
            acc = [mask_pat.parse(line).fixed[0]]
        else:
            addr, val = map(int, set_pat.parse(line).fixed)
            acc.append((addr, val))
    instructions.append(acc)
    return instructions


def read() -> List[str]:
    with open("input.txt") as f:
        return f.read().splitlines()


def solve_one(puzzle):
    mem = defaultdict(int)
    for chunk in puzzle:
        mask, instr = chunk[0], chunk[1:]
        for addr, value in instr:
            val = 0
            for i in range(36):
                c = mask[~i]
                # if 1 in mask or a high bit X then OR the bit
                if c == "1" or (c == 'X' and (value & (1 << i)) > 0):
                    val |= (1 << i)
            mem[addr] = val
    return sum(mem.values())


def solve_two(puzzle):
    mem = defaultdict(int)
    for chunk in puzzle:
        mask, instr = chunk[0], chunk[1:]
        for addr, value in instr:
            print(mask, addr, value)
            variants = []
            new_addr = 0
            for i in range(36):
                c = mask[~i]
                if c == "X":
                    variants.append(1 << i)
                elif c == "1" or (addr & (1 << i) > 0):
                    new_addr += (1 << i)
            # this is way too slow, maybe go back and just use strings?
            print(variants)
            for k in range(len(variants) + 1):
                print("variants start", k)
                for c in itertools.combinations(variants, k):
                    print(c)
            #         offset = sum(c)
            #         print(offset)
            #         print("writing to", new_addr + offset)
            #         mem[new_addr + offset] = value

    return sum(mem.values())





def part_one():
    print('Part one')
    p = parser(read())
    print(p)
    ans = solve_one(p)
    print("ans", ans)


def part_two():
    print('Part two')


if __name__ == '__main__':
    # part_one()
    part_two()
