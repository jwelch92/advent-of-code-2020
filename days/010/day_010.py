from typing import List


def solve_one(puzzle):
    print(puzzle)
    ones, threes = 0, 0
    for i in range(0, len(puzzle) - 1):
        diff = puzzle[i + 1] - puzzle[i]
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
    print(ones, threes)
    return ones * threes


cache = {}


def solve_two(puzzle, i):
    # exit cond
    if i == len(puzzle) - 1:
        return 1
    # memoize results
    if i in cache:
        return cache[i]
    ans = 0
    for j in range(i + 1, len(puzzle)):
        if puzzle[j] - puzzle[i] <= 3:
            ans += solve_two(puzzle, j)
    cache[i] = ans
    return ans


def parse(x: List[str]) -> List[int]:
    raw = list(map(int, x))
    raw.append(0)
    raw.append(max(raw) + 3)
    s = sorted(set(raw))
    return s


def read() -> List[str]:
    with open("input.txt") as f:
        return f.read().splitlines()


def puzzle_input():
    return parse(read())


def part_one():
    print('Part one')
    a = solve_one(puzzle_input())
    print("ans", a)


def part_two():
    print('Part two')
    puz = puzzle_input()
    a = solve_two(puz, 0)
    print("ans", a)


if __name__ == '__main__':
    part_one()
    part_two()
