from dataclasses import dataclass
from parse import compile
from typing import Callable, Iterable

pat = compile("{minimum}-{maximum} {letter}: {password}")


@dataclass
class PasswordEntry:
    minimum: int
    maximum: int
    letter: str
    password: str

    def __post_init__(self):
        self.maximum = int(self.maximum)
        self.minimum = int(self.minimum)

    def count_within_range(self) -> bool:
        count = self.password.count(self.letter)
        return self.minimum <= count <= self.maximum

    def positional_validation(self) -> bool:
        first = self.minimum - 1 if self.minimum > 0 else self.minimum
        last = self.maximum - 1
        try:
            return (self.password[first] == self.letter) != (self.password[last] == self.letter)
        except IndexError:
            return False


def read(parser_func: Callable) -> Iterable[PasswordEntry]:
    with open('input.txt') as f:
        for line in f.readlines():
            yield parser_func(line)


def parser(line: str) -> PasswordEntry:
    g = pat.parse_for_one(line.strip())
    return PasswordEntry(**g.named)


def part_one():
    print('Part one')
    valid = [x for x in read(parser) if x.count_within_range()]
    print(len(valid))


def part_two():
    print('Part two')
    valid = [x for x in read(parser) if x.positional_validation()]
    print(len(valid))


if __name__ == '__main__':
    part_one()
    part_two()
