from .vertex import Vertex


class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, distance: float = 1.0):
        self.vertices = (v1, v2)
        self.distance = distance
        self._name = f"{v1.name}-{v2.name}:{distance}"

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return self._name == other.name

    def __contains__(self, item):
        for item in self.vertices:
            if item.name == self._name:
                return True
        return False

    def __str__(self):
        return self._name
