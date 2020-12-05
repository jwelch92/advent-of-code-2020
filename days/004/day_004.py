import re
from typing import List, Dict

fields = [
    ("byr", True, lambda x: 1920 <= int(x) <= 2002),  # four digits; at least 1920 and at most 2002.
    ("iyr", True, lambda x: 2010 <= int(x) <= 2020),  # four digits; at least 2010 and at most 2020.
    ("eyr", True, lambda x: 2020 <= int(x) <= 2030),  # four digits; at least 2020 and at most 2030.
    ("hgt", True, lambda x: 150 <= int(x.replace("cm", "")) <= 193 if "cm" in x else 59 <= int(
        x.replace("in", "")) <= 76 if "in" in x else False),
    ("hcl", True, lambda x: re.match(r'#[a-z0-9]{6}', x)),  # a # followed by exactly six characters 0-9 or a-f.
    ("ecl", True, lambda x: x in "amb blu brn gry grn hzl oth".split(" ")),
    # exactly one of: amb blu brn gry grn hzl oth.
    ("pid", True, lambda x: len(x) == 9 and int(x.lstrip("0"))),  # a nine-digit number, including leading zeroes.
    ("cid", False, lambda x: x),  # ignored, missing or not.
]


def read() -> List[str]:
    output = []
    with open('input.txt') as f:
        acc = ""
        for line in f.readlines():
            if line != "\n":
                if len(acc) > 0:
                    acc += " "
                acc += line.strip()
            else:
                output.append(acc.strip())
                acc = ""
        else:
            output.append(acc)
    return output


def validate_part_one(passport) -> bool:
    for field, required, _ in fields:
        if field not in passport and required:
            return False
    return True


def part_one():
    print('Part one')
    valid = [x for x in read() if validate_part_one(x)]
    print("Total valid", len(valid))


def to_fields(passport: str) -> Dict[str, str]:
    return {x.split(":")[0]: x.split(":")[1] for x in passport.split(" ")}


def validate_part_two(passport: str) -> bool:
    p = to_fields(passport)
    for field, required, validator in fields:
        if required and (field not in p.keys() or not validator(p[field])):
            return False
    return True


def part_two():
    print('Part two')
    valid = [x for x in read() if validate_part_two(x)]
    print("Total valid", len(valid))


if __name__ == '__main__':
    part_one()
    part_two()
