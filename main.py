from graph import Graph
from greedy import Greedy
from backtracking import Backtracking

# get a valid colouring with greedy
graph = Graph({1, 2, 3, 4}, {(1, 2), (2, 3), (1, 3), (3, 4)})
greedy = Greedy(graph)
print(greedy.colour())

# get a valid colouring with backtracking
backtracking = Backtracking(graph, 3)
print(backtracking.colour())

# get chromatic number
k = 1
backtracking = Backtracking(graph, k)
while backtracking.colour() is None:
    k += 1
    backtracking = Backtracking(graph, k)
print(k)