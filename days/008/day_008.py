from dataclasses import dataclass
from typing import List

import parse


def read() -> List[str]:
    with open('input.txt') as f:
        return [x.strip() for x in f.readlines()]


@dataclass
class Instruction:
    op: str
    data: int
    marked: bool

    @classmethod
    def from_instruction(cls, line: str) -> "Instruction":
        parsed = parse.parse("{op} {data:d}", line)
        return cls(op=parsed.named["op"], data=parsed.named["data"], marked=False)

    def mark(self):
        self.marked = True

    def reset(self):
        self.marked = False

    def repair(self):
        if self.op == "jmp":
            self.op = "nop"
        elif self.op == "nop":
            self.op = "jmp"


Program = List[Instruction]


class InfiniteLoopError(Exception):
    pass


class ProgramComplete(Exception):
    pass


class Machine:
    def __init__(self, program: Program):
        self.acc: int = 0
        self.cursor: int = 0
        self.program: Program = program

    def boot(self):
        self.acc = 0
        self.cursor = 0
        for i in self.program:
            i.reset()

    def execute(self):
        self._execute_program(self.program)

    def _execute_program(self, program: Program):
        while True:
            try:
                inst = program[self.cursor]
            except IndexError:
                raise ProgramComplete

            if inst.marked:
                raise InfiniteLoopError

            if inst.op == "acc":
                self._handle_acc(inst)
            elif inst.op == "jmp":
                self._handle_jmp(inst)
            else:
                self._handle_nop(inst)

            inst.mark()
            self.print_debug()

    def debug_infinite(self):
        candidate_instructions = [i for i, instruction in enumerate(self.program) if instruction.op in ("jmp", "nop")]

        for index in candidate_instructions:
            print("repairing ", index)
            program = self.program
            try:
                program[index].repair()
                self.boot()
                self._execute_program(program)
                program[index].repair()
            except InfiniteLoopError:
                program[index].repair()

    def _handle_acc(self, inst: Instruction):
        self.acc += inst.data
        self.cursor += 1

    def _handle_jmp(self, inst: Instruction):
        self.cursor += inst.data

    def _handle_nop(self, inst: Instruction):
        self.cursor += 1

    def print_debug(self):
        print(f"cursor={self.cursor} acc={self.acc}")


def part_one():
    print('Part one')
    m = Machine([Instruction.from_instruction(line) for line in read()])
    try:
        m.execute()
    except InfiniteLoopError:
        print("acc", m.acc)


def part_two():
    print('Part two')
    m = Machine([Instruction.from_instruction(line) for line in read()])
    try:
        m.debug_infinite()
    except ProgramComplete:
        print("acc", m.acc)


if __name__ == '__main__':
    part_one()
    part_two()
