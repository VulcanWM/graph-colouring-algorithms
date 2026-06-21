class Graph:
    def __init__(self, vertices, edges):
        self.vertices = set(vertices)
        self.edges = set(edges)

    def get_neighbours(self, vertex):
        neighbours = set()
        for edge in self.edges:
            if vertex in edge:
                current_vertex_index = edge.index(vertex)
                neighbour = edge[1-current_vertex_index]
                neighbours.add(neighbour)
        return neighbours

    def get_degree(self, vertex):
        return len(self.get_neighbours(vertex))