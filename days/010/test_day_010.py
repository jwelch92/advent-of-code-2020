import unittest

from .day_010 import solve_one, solve_two, parse

puzzle_input = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        expected_output = 220
        self.assertEqual(solve_one(parse(puzzle_input.splitlines())), expected_output)

    def test_part_two(self):
        self.assertEqual(solve_two(parse(puzzle_input.splitlines()), 0), 19208)


if __name__ == '__main__':
    unittest.main()
