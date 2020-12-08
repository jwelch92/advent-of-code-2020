import unittest

from .day_008 import Machine, Frame, Instruction

class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        puzzle_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""
        expected_output = 5 # value in acc before infinite loop
        m = Machine()
        acc = m.run_part_one(puzzle_input.splitlines())
        print(acc)
        self.assertEqual(acc, expected_output)



if __name__ == '__main__':
    unittest.main()
