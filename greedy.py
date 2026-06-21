from graph import Graph

class Greedy:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.colourings = {}

    def colour(self):
        self.colourings = {}
        for vertex in self.graph.vertices:
            colour = 0
            valid_colouring = False
            while not valid_colouring:
                colour += 1
                valid_colouring = True
                for neighbour in self.graph.get_neighbours(vertex):
                    if self.colourings.get(neighbour, 0) == colour:
                        valid_colouring = False
            self.colourings[vertex] = colour