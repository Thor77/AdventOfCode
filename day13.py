from itertools import permutations, tee
from re import compile


def seating_arrangements(influence_list):
    guests = list(influence_list.keys())
    seating_arrangements = []
    for permutation in permutations(guests):
        permutation = list(permutation)
        permutation.append(permutation[0])
        total_change = 0
        p1, p2 = tee(permutation)
        next(p2, None)
        for p1, p2 in zip(p1, p2):
            neighbour_change = influence_list[p1][p2] + influence_list[p2][p1]
            total_change += neighbour_change
        seating_arrangements.append((total_change, permutation))
    return seating_arrangements

parse_re = compile(r'(\w+)\ would\ (gain|lose)\ (\d+).*to\ (\w+)')


def parse_line(line):
    name, operator, influence, neighbour = parse_re.match(line).groups()
    influence = -int(influence) if operator == 'lose' else int(influence)
    return name, influence, neighbour

if __name__ == '__main__':
    influence_list = {}
    part2 = True
    with open('input/13') as f:
        for line in f:
            name, influence, neighbour = parse_line(line.rstrip('\n'))
            influence_list.setdefault(name, {})[neighbour] = influence
    if part2:
        names = list(influence_list.keys())
        for name in names:
            influence_list[name]['myself'] = 0
            influence_list.setdefault('myself', {})[name] = 0
    print(sorted(seating_arrangements(influence_list), key=lambda x: x[0])[-1])
