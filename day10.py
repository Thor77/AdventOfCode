from itertools import groupby


def look_and_say(puzzle_input):
    output = [str(len(list(group))) + number for number, group in groupby(puzzle_input)]
    return ''.join(output)

with open('input/10') as f:
    puzzle_input = f.read().rstrip('\n')
    answer = puzzle_input
    for _ in range(50):
        answer = look_and_say(answer)
    print(len(answer))
