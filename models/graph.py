from typing import List

from .edge import Edge
from .vertex import Vertex


class Graph:
    def __init__(self, vertices: List[Vertex] = None, edges: List[Edge] = None):
        self.vertices = vertices if vertices else []
        self.edges = edges if edges else []
