import math
from typing import Callable, Iterable, Any, List, Tuple

TREE = '#'


def read(parser: Callable) -> Iterable[Any]:
    with open('input.txt') as f:
        for line in f.readlines():
            yield parser(line)


def traverse(data: List[List], moves: List[Tuple[int, int]]) -> List[int]:
    n, m = len(data), len(data[0])
    answers = []
    for dx, dy in moves:
        cur = 0
        x, y = 0, 0
        while x < n:
            cur += data[x][y] == TREE
            x += dx
            y += dy
            y %= m

        answers.append(cur)
    return answers


def part_one():
    print('Part one')
    data = [x for x in read(lambda x: list(x.strip()))]
    print(traverse(data, [(1, 3)])[0])


def part_two():
    print('Part two')
    data = [x for x in read(lambda x: list(x.strip()))]
    moves = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    ans = traverse(data, moves)
    print(math.prod(ans))


if __name__ == '__main__':
    part_one()
    part_two()
