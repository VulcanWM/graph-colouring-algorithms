from graph import Graph

class Greedy:
    def __init__(self, graph: Graph):
        self.graph = graph

    def colour(self):
        colouring = {}
        for vertex in self.graph.vertices:
            colour = 0
            valid_colouring = False
            while not valid_colouring:
                colour += 1
                valid_colouring = True
                for neighbour in self.graph.get_neighbours(vertex):
                    if colouring.get(neighbour, 0) == colour:
                        valid_colouring = False
            colouring[vertex] = colour
        return colouring