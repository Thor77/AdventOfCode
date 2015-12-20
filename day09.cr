def parse_line line
  cities, distance = line.split " = "
  city1, city2 = cities.split " to "
  {city1, city2, distance}
end

cities = [] of String
graph = {} of String => Hash(String, Int32)

File.each_line "input/09" do |line|
  source, dest, distance = parse_line line.chomp '\n'
  cities << source
  cities << dest
  (graph[source] ||= {} of String => Int32)[dest] = distance.to_i
  (graph[dest] ||= {} of String => Int32)[source] = distance.to_i
end
# remove duplicate cities
cities.uniq!

distances = [] of Tuple(Int32, Array(String))
cities.each_permutation do |permutation|
  distance = 0
  permutation.each_index do |index|
    if permutation.size > index + 1
      distance += graph[permutation[index]][permutation[index + 1]]
    end
  end
  distances << {distance, permutation}
end
p distances.sort[-1]
