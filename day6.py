with open('input/06') as f:
    instructions = f.readlines()

# create the lights
lights = [[0 for x in range(1000)] for x in range(1000)]

for instruction in instructions:
    instruction_split = instruction.split()
    if instruction_split[0] == 'turn':
        if instruction_split[1] == 'on':
            operator = lambda x: x + 1
        else:
            operator = lambda x: x - 1 if x > 0 else 0
    elif instruction_split[0] == 'toggle':
        operator = lambda x: x + 2
    else:
        continue

    startx, starty = instruction_split[-3].split(',')
    endx, endy = instruction_split[-1].split(',')
    for x in range(int(startx), int(endx) + 1):
        for y in range(int(starty), int(endy) + 1):
            value = lights[x][y]
            lights[x][y] = operator(value)

lit_lights = sum([len([1 for light in y_lights if light]) for y_lights in lights])
print('lit lights', lit_lights)

total_brightness = sum([sum([light for light in y_lights]) for y_lights in lights])
print('total brightness', total_brightness)
