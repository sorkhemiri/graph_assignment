class Vertex:
    def __init__(self, name: int):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self._name == other.name
