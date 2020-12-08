from collections import defaultdict
from dataclasses import dataclass, field
from typing import List

import parse


def read() -> List[str]:
    with open('input.txt') as f:
        return [x.strip() for x in f.readlines()]


@dataclass(frozen=True)
class Frame:
    op: str = field(hash=True)
    data: int = field(hash=True)
    acc: int = field(hash=True, default=0)


@dataclass
class Instruction:
    op: str = field(hash=True)
    data: int = field(hash=True)
    index: int = field(hash=True)

    @classmethod
    def from_instruction(cls, index: int, line: str) -> "Instruction":
        parsed = parse.parse("{op} {data:d}", line)
        return cls(index=index, op=parsed.named["op"], data=parsed.named["data"])


class Machine:
    def __init__(self):
        self.acc = 0
        # self.stack: set[Frame] = set()  # maybe make a stack
        self.covered: dict[int, bool] = defaultdict(lambda: False)
        self.cursor = 0

    def run_part_one(self, program):
        while True:
            if self.covered[self.cursor]:
                return self.acc

            self.covered[self.cursor] = True

            line = program[self.cursor]
            inst = Instruction.from_instruction(self.cursor, line)

            if inst.op == "acc":
                self._handle_acc(inst)
            elif inst.op == "jmp":
                self._handle_jmp(inst)
            else:
                self._handle_nop(inst)
            self.debug()

    def _handle_acc(self, inst):
        self.acc += inst.data
        self.cursor += 1

    def _handle_jmp(self, inst):
        self.cursor += inst.data

    def _handle_nop(self, inst):
        self.cursor += 1

    def debug(self):
        print(f"cursor={self.cursor} acc={self.acc}")

def part_one():
    print('Part one')
    m = Machine()
    m.run_part_one(read())



def part_two():
    print('Part two')


if __name__ == '__main__':
    part_one()
    part_two()
