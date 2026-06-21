from graph import Graph

class Greedy:
    def __init__(self, graph: Graph):
        self.graph = graph

    def give_colouring(self):
        colourings = {}
        for vertex in self.graph.vertices:
            colour = 0
            valid_colouring = False
            while not valid_colouring:
                colour += 1
                valid_colouring = True
                for neighbour in self.graph.get_neighbours(vertex):
                    if colourings.get(neighbour, 0) == colour:
                        valid_colouring = False
            colourings[vertex] = colour
        return colourings