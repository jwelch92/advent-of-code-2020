import unittest

from .day_005 import get_seat_id


# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.

class MyTestCase(unittest.TestCase):
    def test_get_seat_id(self):
        expect = [
            ("BFFFBBFRRR", 567),
            ("FFFBBBFRRR", 119),
            ("BBFFBBFRLL", 820)
        ]

        for code, expected in expect:
            self.assertEqual(get_seat_id(code), expected)


if __name__ == '__main__':
    unittest.main()
