import math

graph = [
  [ 0,  7,  9, math.inf, math.inf, 14],
  [ 7,  0, 10, 15, math.inf, math.inf],
  [ 9, 10,  0, 11, math.inf,  2],
  [math.inf, 15, 11,  0,  6, math.inf],
  [math.inf, math.inf, math.inf,  6,  0,  9],
  [14, math.inf,  2, math.inf,  9,  0],
  ]

# beginning of function

def djikstra(graph, initial_node):
  num_nodes = len(graph)
  unvisited = set(range(0, num_nodes))

  distances = [math.inf for _ in range(0, num_nodes)]
  distances[initial_node] = 0

  smallest = (initial_node, math.inf)

  while smallest[0] >= 0:
    current = smallest[0]
    unvisited.remove(current)
    smallest = (-1, math.inf)

    for index in range(0, 6):
      if index in unvisited:
        unvisitedDistance = distances[current] + graph[current][index]

        if unvisitedDistance < distances[index]:
          distances[index] = unvisitedDistance

        if unvisitedDistance < smallest[1]:
          smallest = (index, unvisitedDistance)

  return distances

# end of function

distances = djikstra(graph, 0)
print(distances)