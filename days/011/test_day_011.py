import unittest
from typing import List

from .day_011 import solve_one, solve_two, visualize, search_paths, coords


def to_grid(raw: str) -> List[List[str]]:
    return [list(x) for x in raw.splitlines()]


test_raw = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
test = to_grid(test_raw)

part_one_final_raw = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""
part_one_final = to_grid(part_one_final_raw)

part_two_final_raw = """#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#"""

part_two_final = to_grid(part_two_final_raw)


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        answer, final_grid = solve_one(test)
        self.assertEqual(answer, 37)
        self.assertEqual(part_one_final, final_grid)

    def test_coords(self):
        e = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.assertEqual(coords(0), e)

    def test_search_paths(self):
        e = [(-1, -1), (-2, -2),
             (-1, 0), (-2, 0),
             (-1, 1), (-2, 2),
             (0, -1), (0, -2),
             (0, 1), (0, 2),
             (1, -1), (2, -2),
             (1, 0), (2, 0),
             (1, 1), (2, 2)
             ]
        acc = []
        for ca, cb in coords(0):
            for dx, dy in search_paths(ca, cb, 3):
                acc.append((dx, dy))

        self.assertEqual(e, acc)

    def test_part_two(self):
        answer, final_grid = solve_two(test)
        visualize(final_grid)
        self.assertEqual(answer, 26)
        self.assertEqual(part_two_final, final_grid)


if __name__ == '__main__':
    unittest.main()
