from re import compile

parse_re = compile(r'(\w+).*\ (\d+) km\/s\ .*\ (\d+)\ seconds.*\ (\d+)')


class Reindeer:
    def __init__(self, name, speed, stamina, rest_duration):
        self.name = name
        self.speed = speed
        self.stamina = stamina
        self.__stamina = stamina
        self.rest_duration = rest_duration
        self.__rest_duration = 0
        self.pos = 0
        self.points = 0

    def run(self):
        if not self.__rest_duration:
            if self.__stamina:
                # decrease stamina
                self.__stamina -= 1
                # run
                self.pos += self.speed
            else:
                # set rest-duration
                self.__rest_duration = self.rest_duration - 1
                # reset stamina
                self.__stamina = self.stamina
        else:
            self.__rest_duration -= 1

    def __repr__(self):
        return '{}=>{}km|{}P'.format(self.name, self.pos, self.points)


def race(reindeers, seconds):
    for i in range(seconds + 1):
        for reindeer in reindeers:
            reindeer.run()
        # give points to leading reindeers
        leading_reindeers = sorted(reindeers, key=lambda r: r.pos, reverse=True)
        leading_reindeers[0].points += 1
        for lr in leading_reindeers[1:]:
            if lr.pos == leading_reindeers[0].pos:
                lr.points += 1
            else:
                break
    return reindeers

if __name__ == '__main__':
    reindeers = []
    with open('input/14') as f:
        for line in f:
            name, speed, stamina, rest_duration = \
                parse_re.match(line.rstrip('\n')).groups()
            reindeers.append(Reindeer(name, int(speed), int(stamina), int(rest_duration)))
    race_results = race(reindeers, 2503)
    print('Winner (distance):', sorted(race_results, key=lambda r: r.pos)[-1])
    print('Winner (points):', sorted(race_results, key=lambda r: r.points)[-1])
