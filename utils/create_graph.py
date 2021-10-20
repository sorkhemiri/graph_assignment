from typing import List

from models import Graph, Vertex, Edge


def create_graph(edges: List[tuple]) -> Graph:
    graph = Graph()
    for item in edges:
        v1 = Vertex(name=item[0])
        v2 = Vertex(name=item[1])
        edge = Edge(v1, v2)
        if v1 not in graph:
            graph.add_vertex(v1)
        if v2 not in graph:
            graph.add_vertex(v2)
        if edge not in graph:
            graph.add_edge(edge)
    return graph
