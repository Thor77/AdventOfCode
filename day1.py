floor = 0
with open('input/01') as f:
    instructions = f.read()
for i, char in enumerate(instructions):
    if char == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(i + 1)
        break
