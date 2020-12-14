import unittest

from .day_014 import parser, solve_one, solve_two

puzzle_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".splitlines()


class MyTestCase(unittest.TestCase):

    def test_parse(self):
        e = [["XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", (8, 11), (7, 101), (8, 0)]]
        self.assertEqual(e, parser(puzzle_input))

    def test_part_one(self):
        p = parser(puzzle_input)
        self.assertEqual(solve_one(p), 165)

    def test_part_two(self):
        p = parser(puzzle_input)
        self.assertEqual(solve_two(p), 208)


if __name__ == '__main__':
    unittest.main()
