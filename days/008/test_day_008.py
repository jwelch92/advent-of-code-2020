import unittest

from .day_008 import Machine, Instruction, InfiniteLoopError


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
        m = Machine([Instruction.from_instruction(line) for line in puzzle_input.splitlines()])

        try:
            m.execute()
        except InfiniteLoopError:
            self.assertEqual(m.acc, expected_output)



if __name__ == '__main__':
    unittest.main()
