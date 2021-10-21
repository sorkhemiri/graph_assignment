from math import isinf
from typing import List

from .edge import Edge
from .vertex import Vertex


class Graph:
    def __init__(self, vertices: List[Vertex] = None, edges: List[Edge] = None):
        self.vertices = vertices if vertices else []
        self.edges = edges if edges else []
        self._shortest_path = [float("inf")] * len(self.vertices)

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

    def min_distance(self, dist: List[float], spt_set: List[bool]):
        minimum = float("inf")
        min_indices = []
        for i, v in enumerate(self.vertices):
            if dist[i] < minimum and spt_set[i] is False:
                minimum = dist[i]
                min_indices = [i]
            elif dist[i] == minimum and spt_set[i] is False:
                min_indices.append(i)
        return min_indices

    def dijkstra(self, v: Vertex):
        dist = [float("inf")] * len(self.vertices)
        vertex_index = self.vertices.index(v)
        dist[vertex_index] = 0
        spt_set = [False] * len(self.vertices)

        for i_vertex in self.vertices:
            inds = self.min_distance(dist, spt_set)
            for ind in inds:
                spt_set[ind] = True
            for ind in inds:
                for j, j_vertex in enumerate(self.vertices):
                    e1 = Edge(self.vertices[ind], j_vertex)
                    e2 = Edge(j_vertex, self.vertices[ind])
                    if (e1 in self or e2 in self) and spt_set[j] is False:
                        if e1 in self and dist[j] > dist[ind] + e1.distance:
                            dist[j] = dist[ind] + e1.distance
                        if e2 in self and dist[j] > dist[ind] + e2.distance:
                            dist[j] = dist[ind] + e2.distance
        self._shortest_path = dist

    def has_broken(self):
        self.dijkstra(self.vertices[0])
        for item in self._shortest_path:
            if isinf(item):
                return True
        return False
