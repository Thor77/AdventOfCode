from operator import __gt__, __lt__, __eq__

from math import inf

target = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def parse_line(line: str):
    name, raw_attrs = line.split(':', 1)
    name_number = int(name.split()[-1])
    attrs = {}
    for attr in raw_attrs.split(','):
        name, value = attr.strip().split(':')
        name = name.strip()
        value = int(value)
        attrs[name] = value
    return name_number, attrs


def part1(lines):
    for line in lines:
        number, attrs = parse_line(line)
        matches = 0
        for name, target_value in target.items():
            if attrs.get(name, -1) == target_value:
                matches += 1
        if matches == len(attrs):
            return number


def part2(lines):
    for line in lines:
        number, attrs = parse_line(line)
        matches = 0
        for name, target_value in target.items():
            default = -1.0
            if name in ['cats', 'trees']:
                op = __gt__
            elif name in ['pomeranians', 'goldfish']:
                op = __lt__
                default = inf
            else:
                op = __eq__
            if op(attrs.get(name, default), target_value):
                matches += 1
        if matches == len(attrs):
            return number


if __name__ == '__main__':
    lines = []
    with open('input/16') as f:
        lines = list(filter(None, map(lambda l: l.rstrip('\n'), f.readlines())))
    print(part1(lines))
    print(part2(lines))
