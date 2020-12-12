import unittest

from .day_012 import solve_one, solve_two

puz = """F10
N3
F7
R90
F11""".splitlines()

class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(solve_one(puz), 25)

    def test_part_two(self):
        self.assertEqual(solve_two(puz), 286)




if __name__ == '__main__':
    unittest.main()
