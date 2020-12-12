import unittest

from .day_011 import solve_one


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
test = [list(x) for x in test_raw.splitlines()]

sample_final_raw = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""

sample_final = [list(x) for x in sample_final_raw.splitlines()]

class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        answer, final_grid = solve_one(test)
        self.assertEqual(answer, 37)
        self.assertEqual(sample_final, final_grid)





if __name__ == '__main__':
    unittest.main()
