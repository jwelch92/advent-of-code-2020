import unittest

from .day_013 import solve_one, solve_two, parse_for_one

puzzle_input = """939
7,13,x,x,59,x,31,19""".splitlines()

part_two_input = "7,13,x,x,59,x,31,19".split(",")

class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(295, solve_one(*parse_for_one(puzzle_input)), 295)


    def test_part_two(self):
        self.assertEqual(1068781, solve_two(part_two_input))

if __name__ == '__main__':
    unittest.main()
