from itertools import cycle

with open('input/03') as f:
    plan = f.read()


class Santa:
    x = 0
    y = 0

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def right(self):
        self.x += 1

    def left(self):
        self.x -= 1

    @property
    def pos(self):
        return (self.x, self.y)

santas = [Santa(), Santa()]
houses = [(0, 0) for santa in santas]

santa_iterator = cycle(santas)
for direction in plan:
    santa = santa_iterator.__next__()
    if direction == '^':
        santa.up()
    elif direction == 'v':
        santa.down()
    elif direction == '>':
        santa.right()
    elif direction == '<':
        santa.left()
    houses.append(santa.pos)
print(len(set(houses)))
