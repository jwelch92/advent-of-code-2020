import itertools
from collections import defaultdict
from typing import List
from functools import reduce
import parse
from bitarray import bitarray, util
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


big_int = 2 ** 36

def bitmask(mask):
    return []

def read() -> List[str]:
    with open("input.txt") as f:
        return f.read().splitlines()

def apply_mask(mask, val):
    pass

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
            variants = []
            new_addr = 0
            for i in range(36):
                c = mask[~i]
                if c == "X":
                    variants.append(1 << i)
                elif c == "1" or (addr & (1 << i) > 0):
                    new_addr += (1 << i)
            for k in range(len(variants) + 1):
                for c in itertools.combinations(variants, k):
                    offset = sum(c)
                    mem[new_addr + offset] = value

    return sum(mem.values())



# dumb attempt at using bitarry to do it "right" but loops and lists are easier actually
# def solve_one(puzzle):
#     mem = {}
#     for s in puzzle:
#         mask, instr = s[0], s[1:]
#         m = list(mask)
#         for i in instr:
#             print(i)
#             ba = util.int2ba(i[1], 36, endian="big")
#             print(ba)
#             for masked, (index, value) in zip(m, enumerate(ba)):
#                 if masked == "X":
#                     continue
#                 if int(masked) == value:
#                     continue
#                 ba[index] |= int(masked)
#             print("masked", ba)
#             to_int = util.ba2int(ba)
#             print(to_int)
#             mem[i[0]] = to_int
#     print(mem)
#     return sum(mem.values())



def part_one():
    print('Part one')
    p = parser(read())
    print(p)
    ans = solve_one(p)
    print("ans", ans)


def part_two():
    print('Part two')



if __name__ == '__main__':
    part_one()
    part_two()
