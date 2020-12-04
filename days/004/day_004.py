import re


def validate_hgt(hgt):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    pass


hcl_re = re.compile(r'#[a-z0-9]{6}')
ecl_values = "amb blu brn gry grn hzl oth".split(" ")

fields = [
    ("byr:", True, lambda x: 1920 <= int(x) <= 2002), # four digits; at least 1920 and at most 2002.
    ("iyr:", True, lambda x: 2010 <= int(x) <= 2020), # four digits; at least 2010 and at most 2020.
    ("eyr:", True, lambda x: 2020 <= int(x) <= 2030), # four digits; at least 2020 and at most 2030.
    ("hgt:", True, validate_hgt),
    ("hcl:", True, lambda x: hcl_re.match(x)),  # a # followed by exactly six characters 0-9 or a-f.
    ("ecl:", True, lambda x: x in ecl_values),  # exactly one of: amb blu brn gry grn hzl oth.
    ("pid:", True, lambda x: len(x) == 9 and int(x.lstrip("0"))),  # a nine-digit number, including leading zeroes.
    ("cid:", False, lambda x: x),  # ignored, missing or not.
]


def read():
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
        output.append(acc)
    return output


def validate_part_one(x):
    for m, req, _ in fields:
        if m not in x and req:
            return False
    return True


def part_one():
    print('Part one')
    lines = read()
    valid = [x for x in lines if validate_part_one(x)]
    print(len(valid))

def get_field(x, f):
    for c in x.split(" "):
        if c.startswith(f):
            return c.split(":")[-1]

def validate_part_two(x):
    for m, req, v in fields:
        if req:
            if m not in x:
                return False
            else:
                return v(get_field(x, m))
    return True


def part_two():
    print('Part two')
    lines = read()
    valid = [x for x in lines if validate_part_two(x)]
    print(len(valid))


if __name__ == '__main__':
    part_one()
    part_two()
