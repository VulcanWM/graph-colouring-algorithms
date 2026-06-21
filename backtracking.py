import copy
from graph import Graph

class Backtracking:
    def __init__(self, graph: Graph, k: int):
        self.graph = graph
        self.k = k
        self.domains = {
            vertex: set(range(1, k + 1))
            for vertex in graph.vertices
        }

    def colour(self):
        if not self.ac3():
            return None
        return self.backtrack(dict())

    def revise(self, x, y):
        changed = False
        for colour_x in self.domains[x].copy():
            possible = False
            for colour_y in self.domains[y]:
                if colour_x != colour_y:
                    possible = True
                    break
            if not possible:
                self.domains[x].remove(colour_x)
                changed = True
        return changed

    def ac3(self, arcs=None):
        if arcs is None:
            arcs = []
            for vertex in self.graph.vertices:
                for neighbour in self.graph.get_neighbours(vertex):
                    arcs.append((vertex, neighbour))
        while len(arcs) != 0:
            x, y = arcs.pop(0)
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                for neighbour in self.graph.get_neighbours(x):
                    if neighbour != y:
                        arcs.append((neighbour, x))
        return True

    def assignment_complete(self, assignment):
        return len(assignment) == len(self.graph.vertices)

    def consistent(self, assignment):
        for vertex in assignment:
            for neighbour in self.graph.get_neighbours(vertex):
                if neighbour in assignment:
                    if assignment[vertex] == assignment[neighbour]:
                        return False
        return True

    def order_domain_values(self, vertex, assignment):
        values = {}
        for colour in self.domains[vertex]:
            ruled_out = 0
            for neighbour in self.graph.get_neighbours(vertex):
                if neighbour in assignment:
                    continue
                for neighbour_colour in self.domains[neighbour]:
                    if colour == neighbour_colour:
                        ruled_out += 1
            values[colour] = ruled_out
        return sorted(values, key=values.get)

    def select_unassigned_variable(self, assignment):
        unassigned = [
            vertex
            for vertex in self.graph.vertices
            if vertex not in assignment
        ]
        return min(
            unassigned,
            key=lambda vertex: (
                len(self.domains[vertex]),
                -self.graph.get_degree(vertex)
            )
        )

    def backtrack(self, assignment):
        if self.assignment_complete(assignment):
            return assignment
        vertex = self.select_unassigned_variable(assignment)
        for colour in self.order_domain_values(vertex, assignment):
            assignment[vertex] = colour
            if self.consistent(assignment):
                old_domains = copy.deepcopy(self.domains)
                self.domains[vertex] = {colour}
                arcs = [
                    (neighbour, vertex)
                    for neighbour in self.graph.get_neighbours(vertex)
                ]
                if self.ac3(arcs):
                    result = self.backtrack(assignment)
                    if result is not None:
                        return result
                self.domains = old_domains
            del assignment[vertex]
        return None