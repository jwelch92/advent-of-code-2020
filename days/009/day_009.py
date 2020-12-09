from dataclasses import dataclass
from typing import List
from itertools import combinations

import parse


def read() -> List[int]:
    with open('input.txt') as f:
        return [int(x.strip()) for x in f.readlines()]


def part_one():
    print('Part one')
    xmas = read()
    for i in range(25, len(xmas)):
        print(i)
        cur = xmas[i]
        c = combinations(xmas[i-25:i], 2)

        for a, b in c:
            if a + b == cur:
                break
        else:
            print("did not find a pair for", cur)
            break




def part_two():
    print('Part two')
    # --- Part Two ---
    # The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
    #
    # Again consider the above example:
    #
    # 35
    # 20
    # 15
    # 25
    # 47
    # 40
    # 62
    # 55
    # 65
    # 95
    # 102
    # 117
    # 150
    # 182
    # 127
    # 219
    # 299
    # 277
    # 309
    # 576
    # In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)
    #
    # To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.
    #
    # What is the encryption weakness in your XMAS-encrypted list of numbers?

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
            print("found")
            print(i, running_index)
            r = xmas[i: running_index]
            print(r)
            print(sum(r))
            print(r == magic)


            print("ans", min(r) + max(r))
            break




if __name__ == '__main__':
    # part_one()
    part_two()
