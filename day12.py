from re import finditer
from json import loads


def part1(data):
    return sum(int(number.group(0)) for number in finditer(r'[-]?\d+', data))


def sum_ints(data):
    if type(data) == list:
        values = data
    else:
        values = data.values()
        if 'red' in values:
            return 0
    c = 0
    for value in values:
        if type(value) in [dict, list]:
            c += sum_ints(value)
        elif type(value) == int:
            c += value
    return c


def part2(data):
    data = loads(data)
    return sum(sum_ints(item) for item in data)

if __name__ == '__main__':
    with open('input/12') as f:
        data = f.read().strip('\n')
    print('Part 1', part1(data), sep=' | ')
    print('Part 2', part2(data), sep=' | ')
