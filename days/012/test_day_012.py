import unittest

from .day_012 import solve_one

class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        puz = """F10
N3
F7
R90
F11""".splitlines()
        self.assertEqual(solve_one(puz), 25)




if __name__ == '__main__':
    unittest.main()
