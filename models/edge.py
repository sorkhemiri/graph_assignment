from .vertex import Vertex


class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, distance: float):
        self.vertices = (v1, v2)
        self.distance = distance
