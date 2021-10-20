from typing import List

from .edge import Edge
from .vertex import Vertex


class Graph:
    def __init__(self, vertices: List[Vertex] = None, edges: List[Edge] = None):
        self.vertices = vertices if vertices else []
        self.edges = edges if edges else []

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def add_vertex(self, vertex: Vertex):
        self.vertices.append(vertex)

    def __contains__(self, item):
        if isinstance(item, Edge):
            for edge in self.edges:
                if item == edge:
                    return True
            return False
        elif isinstance(item, Vertex):
            for vertex in self.vertices:
                if item == vertex:
                    return True
        else:
            return False
