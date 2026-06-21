from graph import Graph
from greedy import Greedy

graph = Graph({1, 2, 3, 4}, {(1, 2), (2, 3), (1, 3), (3, 4)})
greedy = Greedy(graph)
greedy.colour()
print(greedy.colourings)