import unittest

from .day_007 import solve_one, solve_two

puzzle_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".splitlines()

class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        expected_count = 4
        self.assertEqual(solve_one(puzzle_input), expected_count)

    def test_part_two(self):
        expected_count = 32
        self.assertEqual(solve_two(puzzle_input), expected_count)


if __name__ == '__main__':
    unittest.main()
