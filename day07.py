with open('input/07') as f:
    raw_circuit = f.readlines()


def parse_instruction(raw_instruction):
    raw_instruction = raw_instruction.rstrip('\n')
    way, signal = raw_instruction.split(' -> ')
    return (way, signal)

circuit = {}
for instruction in raw_circuit:
    way, signal = parse_instruction(instruction)
    circuit[signal] = way

counts = {}
cache = {}


def solve(signal):
    if signal in cache:
        return cache[signal]
    if signal not in circuit:
        return int(signal)
    way = circuit[signal]
    if way in counts:
        counts[way] += 1
    else:
        counts[way] = 1
    way_split = way.split()
    if len(way_split) == 1:
        try:
            return int(way)
        except ValueError:
            return solve(way)
    if way_split[0] == 'NOT':
        result = ~ solve(way_split[1])
    else:
        operator = way_split[1]
        value1, value2 = way_split[0], way_split[2]
        if operator == 'AND':
            result = solve(value1) & solve(value2)
        elif operator == 'OR':
            result = solve(value1) | solve(value2)
        elif operator == 'LSHIFT':
            result = solve(value1) << int(value2)
        elif operator == 'RSHIFT':
            result = solve(value1) >> int(value2)
    if signal not in cache:
        cache[signal] = result
    return result

if __name__ == '__main__':
    print(solve('a'))
