from itertools import permutations


def parse_line(line):
    cities, distance = line.split(' = ')
    city1, city2 = cities.split(' to ')
    return ((city1, city2), distance)


def route_distance(graph, route):
    distance = 0
    for index, city in enumerate(route):
        if len(permutation) > index + 1:
            distance += graph[city][route[index + 1]]
    return distance


if __name__ == '__main__':
    cities = set()
    graph = {}
    with open('input/09') as f:
        for line in f:
            (city1, city2), distance = parse_line(line.rstrip('\n'))
            cities.add(city1)
            cities.add(city2)
            graph.setdefault(city1, {})[city2] = int(distance)
            graph.setdefault(city2, {})[city1] = int(distance)

    distances = []
    for permutation in permutations(cities):
        distance = route_distance(graph, permutation)
        distances.append((distance, permutation))
    print(sorted(distances, key=lambda x: x[0])[-1])
