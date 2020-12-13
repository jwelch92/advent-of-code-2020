import unittest

from .day_013 import solve_one, solve_two, parse

puzzle_input = """939
7,13,x,x,59,x,31,19""".splitlines()


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(295, solve_one(*parse(puzzle_input)), 295)


    def test_part_two(self):
        pass


if __name__ == '__main__':
    unittest.main()
